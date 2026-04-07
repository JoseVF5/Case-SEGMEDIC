select
	id_paciente,
	SUM(case when especialidade = 'Psiquiatria' then valor else 0 END) as psiq_faturamento,
	SUM(case when especialidade = 'Clínica Geral'then valor else 0 END) as clin_geral_faturamento,
	SUM(case when especialidade = 'Endocrinologia'then valor else 0 END) as endo_faturamento,
	COUNT(id_agendamento) as quant_agendamentos
from
	atendimentos
where 
	id_paciente is not null
group by 
	id_paciente
order by
  	 clin_geral_faturamento desc
limit 10;