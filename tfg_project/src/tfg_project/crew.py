from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import VisionTool
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

@CrewBase
class TfgProject():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    json_humanidades = JSONKnowledgeSource(
        file_path='cafeteria_humanidades_info.json',
        knowledge_source_name='cafeteria_humanidades',
        verbose=True,
    )
        
    


    @agent
    def overseer(self) -> Agent:
        return Agent(
            config=self.agents_config['overseer'],
            verbose=True,
            tools=[
                VisionTool(description= "This tool uses OpenAI's Vision API to describe the contents of an image. The image is /app/tfg_project/images/plano_uni.jpg"
                ),
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
                #JSONSearchTool(description= "A tool that can be used to semantic search a query from a JSON's content. The JSON is "
                #"/app/tfg_project/json/cafeteria_volumen_final_corrected.json"),
            ],
            knowledge_sources=[
                self.json_humanidades,
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
