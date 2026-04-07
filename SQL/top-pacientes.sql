select 
    id_paciente,
    SUM(valor) as faturamento,
    COUNT(id_agendamento) as quant_atendimentos
from
    atendimentos
where
    especialidade in ('Psiquiatria', 'Clínica Geral', 'Endocrinologia') 
group by
    id_paciente
order by
    faturamento desc,
    quant_atendimentos desc
limit 10;