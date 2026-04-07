select
	procedimento,
	especialidade,
	SUM(valor) as faturamento
from
	atendimentos
where 
	especialidade != 'NULL'
	and procedimento != 'NULL'
group by 
	procedimento, especialidade;