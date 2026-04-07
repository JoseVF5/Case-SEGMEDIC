select
    pub.cidade,
    pub.sexo,
    SUM(aten.valor) AS faturamento,
    COUNT(aten.id_agendamento) AS quant_atendimentos
FROM
    atendimentos aten
INNER JOIN 
    clientes pub ON aten.id_paciente = pub.id_paciente
WHERE
    aten.especialidade is not null
GROUP BY
    pub.cidade,
    pub.sexo
ORDER BY
    faturamento desc,
    quant_atendimentos desc
LIMIT 10;