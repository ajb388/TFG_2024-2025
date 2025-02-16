from crewai import Crew,Process
from python_files.crewai_folder.tasks import research_task,write_task
from python_files.crewai_folder.agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)