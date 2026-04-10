# Case Técnico - Estágio em Dados: Segmedic

Este repositório contém a minha solução para o Desafio Técnico da Segmedic. O objetivo principal deste projeto é explorar, investigar e estruturar dados de atendimentos clínicos para gerar insights operacionais e financeiros, respondendo a perguntas cruciais de negócio.

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Análise Exploratória:** Python (Pandas)
* **Banco de Dados & Consultas:** SQL (PostgreSQL)
* **Visualização de Dados (BI):** Streamlit

---

## 📂 Estrutura do Projeto

O desafio foi dividido em três etapas principais de análise:

### Parte 1: Análise Exploratória de Dados (EDA) com Python
Nesta etapa, foi realizada uma investigação profunda da estrutura dos dados fornecidos em formato CSV. O foco foi:
* Identificar a estrutura do dataset (linhas, colunas e visualização inicial).
* Calcular o valor total atendido e a quantidade de atendimentos por mês.
* Mapear os Top 5 pacientes com maior frequência de uso da clínica.

*Obs: A abordagem completa, os códigos utilizados e os gráficos gerados estão detalhados no arquivo Jupyter Notebook.*

### Parte 2: Consultas Analíticas com SQL
Conectando ao banco de dados PostgreSQL, foram desenvolvidas queries analíticas para responder às seguintes demandas de negócio:
* Faturamento total e quantidade de atendimentos por especialidade.
* Ranqueamento dos Top 10 pacientes (por valor faturado e quantidade de atendimentos) especificamente para Psiquiatria, Clínica Geral e Endocrinologia.
* Mapeamento das Top cidades geradoras de receita e volume de atendimentos.
* Faturamento isolado da cidade do Rio de Janeiro.
* Análise de retenção listando pacientes que foram atendidos uma vez e retornaram no mês seguinte.

### Parte 3: Dashboard Analítico (BI)
Foi construído um painel interativo focado em quatro pilares principais da operação:
1. **Métricas de Atendimento:** Volume e valor distribuídos por datas e especialidades.
2. **Métricas Financeiras:** Ticket médio por paciente e faturamento consolidado por especialidade.
3. **Perfil dos Pacientes:** Distribuição demográfica por sexo e cidade, além da média histórica de atendimentos por paciente.
4. **Operação da Clínica:** Fluxo diário (quantidade) de consultas realizadas.

---

## 📦 Entregáveis do Repositório

* 📓 `notebook_eda.ipynb`: Arquivo Jupyter Notebook contendo toda a Análise Exploratória (Parte 1).
* 🗄️ `queries_analiticas.sql`: Arquivo contendo todas as consultas SQL desenvolvidas (Parte 2).
* 📄 `Insights_Resumo.pdf`: Documento com o resumo executivo detalhando os principais insights encontrados durante a análise.
* 📊 **Dashboard:**  https://dashpy-obwv7xlmbrrpg7ekyqwfru.streamlit.app/.

---

## 🎯 Foco da Avaliação
Este projeto foi desenvolvido com foco em demonstrar:
* Capacidade investigativa e curiosidade sobre o comportamento dos dados clínicos e financeiros.
* Organização de código estruturado e documentado.
* Raciocínio analítico para transformar dados brutos em informações úteis e estratégicas para o negócio.
* Clareza e objetividade na comunicação visual e escrita dos resultados obtidos.

---
*Desenvolvido por Jose.*
