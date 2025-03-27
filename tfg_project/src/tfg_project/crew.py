from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tfg_project.tools.custom_tool import MyCustomTool
from tfg_project.tools.json_reader_tool import JsonReaderTool, JsonReaderInput

@CrewBase
class TfgProyect():

	#Configuracion de los llm
	deepseek_llm = LLM(
		model= 'ollama/deepseek-r1:14b',
		base_url = 'http://localhost:11434',
		temperature=0
	)

	mistral_llm = LLM(
		model= 'ollama/mistral:latest',
		base_url = 'http://localhost:11434',
	)

	llama_llm = LLM(
		model= 'ollama/llama3.2:latest',
		base_url = 'http://localhost:11434',
	)

	#Configuracion de los agentes y tareas
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	

	@agent
	def overseer(self) -> Agent:
		return Agent(
			config=self.agents_config['overseer'],
			verbose=True,
			allow_delegation=True,
			tools=[
				MyCustomTool(target_agent=self.coffeewatch()),
				#MyCustomTool(target_agent=self.classflow()) 
			],
		llm=self.deepseek_llm
		)


	@agent
	def coffeewatch(self) -> Agent:
		return Agent(
			config=self.agents_config['coffeewatch'],
			verbose=True,
			tools=[
				JsonReaderTool()
			],
			llm=self.deepseek_llm
		)
	
	@agent
	def classflow(self) -> Agent:
		return Agent(
			config=self.agents_config['classflow'],
			verbose=True,
			llm=self.deepseek_llm
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
			agents=[
				self.overseer(),
				self.coffeewatch(),
			],
			tasks=[
				self.responder_pregunta_overseer()
			],
			verbose=True,
			process=Process.sequential,
		)
