from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import VisionTool, JSONSearchTool

@CrewBase
class TfgProject():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def overseer(self) -> Agent:
        return Agent(
            config=self.agents_config['overseer'],
            verbose=True,
            
        )

    @agent
    def coffeewatch(self) -> Agent:
        return Agent(
            config=self.agents_config['coffeewatch'],
            verbose=True,
            tools=[
                VisionTool(description= "This tool uses OpenAI's Vision API to describe the contents of an image. The image is /app/tfg_project/images/cafeteria_humanidades.jpg"),
                #JSONSearchTool(description= "A tool that can be used to semantic search a query from a JSON's content. The JSON is "
                #"/app/tfg_project/json/cafeteria_volumen_final_corrected.json"),
            ],

        )

    @task
    def obtener_informacion_cofeewatch(self) -> Task:
        return Task(
            config=self.tasks_config['obtener_informacion_cofeewatch'],
            
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
