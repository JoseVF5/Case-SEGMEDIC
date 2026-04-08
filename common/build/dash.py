import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard Clínico", layout="wide")

st.title("Dashboard Desafio Técnico - Segmedic")

# Tratar novamente os dados para evitar erro com a exportação do Dbeaver
@st.cache_data
def load_data():
    try:
        # Lê o CSV unificado
        df = pd.read_csv(r'/home/jvdata/Documentos/Case-SEGMEDIC/src/data/ouro/dados_dashboard.csv', sep =";")
        
        # Converte a coluna de data para o tipo datetime do Pandas
        df['data_atendimento'] = pd.to_datetime(df['data_atendimento']).dt.date
        
        # Preenche valores vazios caso existam
        df['especialidade'] = df['especialidade'].fillna('Não Informada')
        df['sexo'] = df['sexo'].fillna('Não Informado')
        df['cidade'] = df['cidade'].fillna('Não Informada')
        
        return df
    except FileNotFoundError:
        st.error("⚠️ Arquivo 'dados_dashboard.csv' não encontrado. Verifique a pasta.")
        return pd.DataFrame()

df_raw = load_data()

if df_raw.empty:
    st.stop() # Para a execução se não tiver dados. Focado na prevenção de erros

# SideBar e Filtros dinâmicos
st.sidebar.header("Filtros")

# Filtro de Data
data_min = df_raw['data_atendimento'].min()
data_max = df_raw['data_atendimento'].max()

filtro_data = st.sidebar.date_input(
    "Período de Atendimento",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max
)

# Filtro de Especialidade
lista_especialidades = df_raw['especialidade'].unique().tolist()
filtro_espec = st.sidebar.multiselect(
    "Especialidades",
    options=lista_especialidades,
    default=lista_especialidades # Vem toda seleção como padrão
)

# Filtro de Cidade
lista_cidades = df_raw['cidade'].unique().tolist()
filtro_cidade = st.sidebar.multiselect(
    "Cidades",
    options=lista_cidades,
    default=lista_cidades
)

# Aplica os Filtros
# Tenta aplicar o filtro de data e tratar o erro caso o usuário selecione apenas 1 dia no calendário
if len(filtro_data) == 2:
    start_date, end_date = filtro_data
else:
    start_date = end_date = filtro_data[0]

df_filtered = df_raw[
    (df_raw['data_atendimento'] >= start_date) &
    (df_raw['data_atendimento'] <= end_date) &
    (df_raw['especialidade'].isin(filtro_espec)) &
    (df_raw['cidade'].isin(filtro_cidade))
]

# Estrutura do Dashboard

tab1, tab2, tab3, tab4 = st.tabs([
    "Métricas de Atendimento", 
    "Métricas Financeiras", 
    "Perfil dos Pacientes", 
    "Operação da Clínica"
])

# ABA 1: MÉTRICAS DE ATENDIMENTO
with tab1:
    st.header("Métricas de Atendimento")
    st.markdown("Acompanhe o volume e o retorno financeiro diário das consultas.")
    
    df_data = df_filtered.groupby('data_atendimento').agg(
        valor_total=('valor', 'sum'),
        qtd_atendimentos=('id_agendamento', 'count')
    ).reset_index()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Valor por Data de Atendimento")
        fig_val_data = px.area(
            df_data, 
            x='data_atendimento', 
            y='valor_total', 
            markers=True,
            labels={'data_atendimento': 'Data', 'valor_total': 'Faturamento'}
        )
        fig_val_data.update_layout(yaxis_tickprefix="R$ ", yaxis_tickformat=",.2f")
        st.plotly_chart(fig_val_data, use_container_width=True)
        
    with col2:
        st.subheader("Volume de Atendimentos por Data")
        fig_qtd_data = px.bar(
            df_data, 
            x='data_atendimento', 
            y='qtd_atendimentos',
            text_auto=True, 
            labels={'data_atendimento': 'Data', 'qtd_atendimentos': 'Qtd. Consultas'}
        )
        fig_qtd_data.update_traces(textposition='outside')
        fig_qtd_data.update_layout(yaxis_visible=False)
        st.plotly_chart(fig_qtd_data, use_container_width=True)
        
    st.divider()
    
    st.subheader("Quantidade de Atendimentos por Especialidade")
    st.markdown("Ranking do volume de atendimentos entre as diferentes áreas.")
    

    df_espec_qtd = df_filtered.groupby('especialidade')['id_agendamento'].count().reset_index()
    df_espec_qtd = df_espec_qtd.sort_values(by='id_agendamento', ascending=True)
    
    fig_espec = px.bar(
        df_espec_qtd, 
        x='id_agendamento', 
        y='especialidade', 
        orientation='h',
        text_auto=True,
        labels={'id_agendamento': 'Quantidade de Atendimentos', 'especialidade': ''}
    )
    fig_espec.update_traces(textposition='outside')
    fig_espec.update_layout(xaxis_visible=False) # Limpa o eixo X
    st.plotly_chart(fig_espec, use_container_width=True)

# ABA 2: MÉTRICAS FINANCEIRAS
with tab2:
    st.header("Métricas Financeiras")
    
    total_receita = df_filtered['valor'].sum()
    total_pacientes_unicos = df_filtered['id_paciente'].nunique()
    
    # Prevenção de divisão por zero
    ticket_medio = total_receita / total_pacientes_unicos if total_pacientes_unicos > 0 else 0
    
    col_kpi1, col_kpi2 = st.columns(2)
    col_kpi1.metric("Receita Total (Filtro)", f"R$ {total_receita:,.2f}")
    col_kpi2.metric("Ticket Médio por Paciente", f"R$ {ticket_medio:,.2f}")
    
    st.divider()
    st.subheader("Valor e Quantidade de Atendimentos por Especialidade")
    # Agrupando por especialidade
    df_fin_espec = df_filtered.groupby('especialidade').agg(
        valor_total=('valor', 'sum'),
        qtd_atendimentos=('id_agendamento', 'count')
    ).reset_index()
    
    st.dataframe(df_fin_espec.sort_values(by='valor_total', ascending=False), use_container_width=True)

# ABA 3: PERFIL DOS PACIENTES
with tab3:
    st.header("Perfil dos Pacientes")
    
    total_atendimentos = df_filtered['id_agendamento'].count()
    media_atend = total_atendimentos / total_pacientes_unicos if total_pacientes_unicos > 0 else 0
    
    st.metric("Média de Atendimentos por Paciente", f"{media_atend:.2f} visitas")
    st.divider()
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Atendimentos por Sexo")
        df_sexo = df_filtered.groupby('sexo')['id_agendamento'].count().reset_index()
        fig_sexo = px.pie(df_sexo, names='sexo', values='id_agendamento')
        st.plotly_chart(fig_sexo, use_container_width=True)
        
    with col4:
        st.subheader("Atendimentos e Valor por Cidade")
        df_cidade = df_filtered.groupby('cidade').agg(
            qtd_atendimentos=('id_agendamento', 'count'),
            valor_total=('valor', 'sum')
        ).reset_index()
        fig_cidade = px.scatter(df_cidade, x='qtd_atendimentos', y='valor_total', 
                                size='valor_total', color='cidade', hover_name='cidade')
        st.plotly_chart(fig_cidade, use_container_width=True)

# ABA 4: OPERAÇÃO DA CLÍNICA
with tab4:
    st.header("Operação da Clínica")
    st.markdown("Visão geral do volume operacional diário.")
    
    # Utilizando um gráfico de área para ver o volume acumulado de consultas
    fig_operacao = px.area(df_data, x='data_atendimento', y='qtd_atendimentos', 
                           title="Volume de Consultas Realizadas")
    st.plotly_chart(fig_operacao, use_container_width=True)