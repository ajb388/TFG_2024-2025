from crewai import Agent, Crew, Process, Task, Knowledge
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from tfg_project.tools.custom_tool import MyCustomTool  # Importamos la herramienta
@CrewBase
class TfgProyect():
	"""TfgProyect crew"""

	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	json_source_central = JSONKnowledgeSource(
    		file_paths=["cafeteria_central_smooth_min.json"]
			)

	json_source_comedor = JSONKnowledgeSource(
    	file_paths=["comedor_universidad_adjusted.json"]
	)

	# https://docs.crewai.com/concepts/agents#agent-tools
	# Agente principal que tiene la capacidad de delegar tareas a otros agentes
	@agent
	def overseer(self) -> Agent:
		return Agent(
			config=self.agents_config['overseer'],
			verbose=True,
			memory=True,
			allow_delegation=True,
			tools=[
				MyCustomTool(target_agent=self.coffeewatch()),  # 📌 Agregar coffeewatch como herramienta
				MyCustomTool(target_agent=self.classflow())  # 📌 Agregar classflow como herramienta
			]
		)


	@agent
	def coffeewatch(self) -> Agent:
		return Agent(
			config=self.agents_config['coffeewatch'],
			verbose=True,
			knowledge_storage=[self.json_source_central, self.json_source_comedor]
		)
	
	@agent
	def classflow(self) -> Agent:
		return Agent(
			config=self.agents_config['classflow'],
			verbose=True,
		)

	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	
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
			agents=[
				self.overseer(),
				self.coffeewatch(),
				self.classflow()
			],
			tasks=[
				self.responder_pregunta_overseer()
			],
			verbose=True,
			process=Process.sequential,
		)
