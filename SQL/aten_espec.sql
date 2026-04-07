select
    aten.especialidade,
    pub.sexo,
    COUNT(aten.id_agendamento) as quant_atendimentos
from
    atendimentos aten
inner join
    clientes pub on aten.id_paciente = pub.id_paciente
where
    aten.especialidade is not null and pub.sexo is not null
group by
    aten.especialidade,
    pub.sexo
order by
    quant_atendimentos desc;