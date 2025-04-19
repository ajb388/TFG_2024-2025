from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import VisionTool
from tfg_project.tools.custom_tool import GoogleMapsRouteTool, GoogleMapsPlaceSearchTool
from crewai_tools import ScrapeWebsiteTool
from tfg_project.config.files import files as config_files

@CrewBase
class TfgProject():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def overseer(self) -> Agent:
        return Agent(
            config=self.agents_config['overseer'],
            verbose=True,
            allow_delegation=True,
            memory=False,
            tools=[
                GoogleMapsRouteTool(),
                GoogleMapsPlaceSearchTool(),
            ],
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
                config_files.json_humanidades,
                config_files.json_cae,
                config_files.json_central,
                config_files.json_comedor,
                config_files.json_starbucks,
            ],
            memory=False,
        )
    
    @agent
    def classroom_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['classroom_coordinator'],
            verbose=True,
            tools=[
            ],
            knowledge_sources=[
                config_files.json_aulario_1,
                config_files.json_aulario_2,
                config_files.json_aulario_3,
                config_files.json_aulario_4,
                config_files.json_aulario_5,
            ],
            memory=False,
        )
    
    @agent
    def library_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['library_manager'],
            verbose=True,
            tools=[
                ScrapeWebsiteTool(website_url='https://www.ual.es/universidad/serviciosgenerales/biblioteca/prestamo/prestamo-domicilio'),
                ScrapeWebsiteTool(website_url='https://www.ual.es/universidad/serviciosgenerales/biblioteca/prestamo/prestamo-interbibliotecario'),
                ScrapeWebsiteTool(website_url='https://www.ual.es/universidad/serviciosgenerales/biblioteca/formacion'),
                ScrapeWebsiteTool(website_url='https://www.ual.es/universidad/serviciosgenerales/biblioteca/prestamo/prestam-e'),
                ScrapeWebsiteTool(website_url='https://www.ual.es/universidad/serviciosgenerales/biblioteca/servicios'),
            ],
            knowledge_sources=[
                config_files.pdf_biblioteca,
            ],
            memory=False,
        )
    
    @agent
    def parking_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['parking_advisor'],
            verbose=True,
            knowledge_sources=[
                config_files.json_lunes,
                config_files.json_martes,
                config_files.json_miercoles,
                config_files.json_jueves,
                config_files.json_viernes,
                config_files.json_sabado,
                config_files.json_domingo,
            ],
            memory=False,
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
