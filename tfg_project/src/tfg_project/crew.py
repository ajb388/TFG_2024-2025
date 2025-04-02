from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import VisionTool
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from tfg_project.tools.custom_tool import GoogleMapsRouteTool

@CrewBase
class TfgProject():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    json_humanidades = JSONKnowledgeSource(
        file_paths='cafeteria_humanidades.json',
        knowledge_source_name='cafeteria_humanidades',
        verbose=True,
    )

    json_cae = JSONKnowledgeSource(
        file_paths='cafeteria_cae.json',
        knowledge_source_name='cafeteria_cae',
        verbose=True,
    )

    json_central = JSONKnowledgeSource(
        file_paths='cafeteria_central.json',
        knowledge_source_name='cafeteria_central',
        verbose=True,
    )

    json_comedor = JSONKnowledgeSource(
        file_paths='comedor_ual.json',
        knowledge_source_name='comedor',
        verbose=True,
    )

    json_starbucks = JSONKnowledgeSource(
        file_paths='Starbucks_corners.json',
        knowledge_source_name='maquina_starbucks',
        verbose=True,
    )

    json_aulario_1 = JSONKnowledgeSource(
        file_paths='aulario_1.json',
        knowledge_source_name='aulario_1',
        verbose=True,
    )

    json_aulario_2 = JSONKnowledgeSource(
        file_paths='aulario_2.json',
        knowledge_source_name='aulario_2',
        verbose=True,
    )

    json_aulario_3 = JSONKnowledgeSource(
        file_paths='aulario_3.json',
        knowledge_source_name='aulario_3',
        verbose=True,
    )

    json_aulario_4 = JSONKnowledgeSource(
        file_paths='aulario_4.json',
        knowledge_source_name='aulario_4',
        verbose=True,
    )

    json_aulario_5 = JSONKnowledgeSource(
        file_paths='aulario_5.json',
        knowledge_source_name='aulario_5',
        verbose=True,
    )

    @agent
    def overseer(self) -> Agent:
        return Agent(
            config=self.agents_config['overseer'],
            verbose=True,
            tools=[
                GoogleMapsRouteTool()
            ],
            allow_delegation=True,
           
        )

    @agent
    def cafe_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['cafe_expert'],
            verbose=True,
            tools=[
                VisionTool(description= "This tool uses OpenAI's Vision API to describe the contents of an image. The image is /app/tfg_project/images/cafeteria_humanidades.jpg"),
                VisionTool(description= "This tool uses OpenAI's Vision API to describe the contents of an image. The image is /app/tfg_project/images/cafeteria_cae.jpg"),
                VisionTool(description= "This tool uses OpenAI's Vision API to describe the contents of an image. The image is /app/tfg_project/images/cafeteria_central.jpg"),
                VisionTool(description= "This tool uses OpenAI's Vision API to describe the contents of an image. The image is /app/tfg_project/images/comedor_ual.jpg"),
            ],
            knowledge_sources=[
                self.json_comedor,
                self.json_humanidades,
                self.json_cae,
                self.json_central,
                self.json_starbucks,
            ],
        )
    
    @agent
    def classroom_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['classroom_coordinator'],
            verbose=True,
            tools=[
            ],
            knowledge_sources=[
                self.json_aulario_1,
                self.json_aulario_2,
                self.json_aulario_3,
                self.json_aulario_4,
                self.json_aulario_5,
            ],
        )

    @task
    def responder_pregunta_overseer(self) -> Task:
        return Task(
            config=self.tasks_config['responder_pregunta_overseer'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,

        )
