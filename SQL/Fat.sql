select
	especialidade,
	SUM(valor) as faturamento
from
	atendimentos
where 
	especialidade is not NULL
group by 
	especialidade
order by
    faturamento ASC;