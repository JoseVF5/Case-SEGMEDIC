with ContagemMensal as (
    -- quantos atendimentos cada paciente teve por mês e ano juntando tudo na janela de exibição para uso
    select 
        id_paciente,
        extract(year from data_atendimento) as ano,
        extract(year from data_atendimento) as mes,
        count(id_agendamento) as total_atendimentos
    from 
        atendimentos
    group by
        id_paciente, 
        extract(year from data_atendimento),
        extract(year from data_atendimento)
)

-- Listar os pacientes cruzando o mês de visita única com o mês seguinte, ou seja, mês + 1
select distinct  
    mes_atual.id_paciente
from 
    ContagemMensal mes_atual
inner join 
    ContagemMensal mes_seguinte 
    on mes_atual.id_paciente = mes_seguinte.id_paciente
where 
    -- Atender apenas uma vez no mês atual
    mes_atual.total_atendimentos = 1
    
    -- Retornar no mês seguinte, isso com a virada de ano
    and (
        (mes_seguinte.ano = mes_atual.ano and mes_seguinte.mes = mes_atual.mes + 1)
        or 
        (mes_atual.mes = 12 and mes_seguinte.mes = 1 and mes_seguinte.ano = mes_atual.ano + 1)
    );