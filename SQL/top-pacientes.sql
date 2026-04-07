select
	id_paciente,
	SUM(valor) filter (where especialidade =  'Psiquiatria')  psiq_faturamento,
	SUM(valor) filter (where especialidade =  'Clínica Geral')  clinica_faturamento,
	COUNT(id_agendamento) as quant_agendamentos
from
	atendimentos
where 
	id_paciente is not null
group by 
	id_paciente
order by
  	 psiq_faturamento desc limit 10;