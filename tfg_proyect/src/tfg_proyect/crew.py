from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

@CrewBase
class TfgProyect():
	"""TfgProyect crew"""

	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	

	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def overseer(self) -> Agent:
		return Agent(
			config=self.agents_config['overseer'],
			verbose=True,
			memory=True,
			llm = "ollama/mistral"

		)

	@agent
	def cofeewatch(self) -> Agent:
		json_source_central = JSONKnowledgeSource(
    		file_paths=["json/central/cafeteria_central_smooth_min.json"]
			)

		json_source_comedor = JSONKnowledgeSource(
    		file_paths=["json/comedor/comedor_universidad_adjusted.json"]
		)
		return Agent(
			config=self.agents_config['cofeewatch'],
			verbose=True,
			llm = "ollama/mistral",
			knowledge_sources= [json_source_comedor, json_source_central]

		)
	
	@agent
	def classflow(self) -> Agent:
		json_source_humanidades = JSONKnowledgeSource(
    		file_paths=["json/humanidades/cafeteria_humanidades_smooth_friday.json"]
		)
		return Agent(
			config=self.agents_config['classflow'],
			verbose=True,
			llm = "ollama/mistral",
			knowledge_sources= [json_source_humanidades]

		)

	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def seleccion_agente(self) -> Task:
		return Task(
			config=self.tasks_config['seleccion_agente'],
		)

	@task
	def responder_pregunta(self) -> Task:
		return Task(
			config=self.tasks_config['responder_pregunta'],
		)
	
	@task
	def obtener_informacion_cofeewatch(self) -> Task:
		return Task(
			config=self.tasks_config['obtener_informacion_cofeewatch'],
		)
	
	@task
	def obtener_informacion_classflow(self) -> Task:
		return Task(
			config=self.tasks_config['obtener_informacion_classflow'],
		)

	@task
	def responder_pregunta_overseer(self) -> Task:
		return Task(
			config=self.tasks_config['responder_pregunta_overseer'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TfgProyect crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			verbose=True,
			process=Process.hierarchical
		)
