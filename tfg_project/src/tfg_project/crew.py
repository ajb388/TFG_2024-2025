from crewai import Agent, Crew, Process, Task, Knowledge
from crewai.project import CrewBase, agent, crew, task, tool
from tfg_project.tools.custom_tool import MyCustomTool
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
import os
@CrewBase
class TfgProyect():
	"""TfgProyect crew"""

	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	

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
				MyCustomTool(target_agent=self.coffeewatch()),
				MyCustomTool(target_agent=self.classflow()) 
			]
		)


	@agent
	def coffeewatch(self) -> Agent:
		return Agent(
			config=self.agents_config['coffeewatch'],
			verbose=True,
			memory=True,
		)
	
	@agent
	def classflow(self) -> Agent:
		return Agent(
			config=self.agents_config['classflow'],
			verbose=True,
			memory=True,
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
				self.classflow()
			],
			tasks=[
				self.responder_pregunta_overseer()
			],
			verbose=True,
			process=Process.sequential,
		)
