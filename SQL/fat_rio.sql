select
    pub.cidade,
    SUM(valor) as faturamento_rio
from
    atendimentos aten
inner join
    clientes pub on aten.id_paciente = pub.id_paciente
where
    cidade = 'Rio De Janeiro '
group by
    pub.cidade
order by
    faturamento_rio desc;