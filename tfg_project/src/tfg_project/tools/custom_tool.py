from crewai.tools import BaseTool
from crewai import Agent, Task
from typing import Type
from pydantic import BaseModel, Field

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    question: str = Field(..., description="Pregunta que se enviará al agente.")

class MyCustomTool(BaseTool):
    name: str = "Pregunta a otro agente"
    description: str = "Esta herramienta permite al overseer preguntar a otros agentes."
    args_schema: Type[BaseModel] = MyCustomToolInput
    target_agent: Agent  # 📌 Aquí almacenamos el agente al que preguntaremos

    def _run(self, question: str) -> str:
        """Envía una pregunta al agente objetivo y obtiene una respuesta."""
        temp_task = Task(
            description=f"Responder a la pregunta: {question}",
            expected_output="Una respuesta clara y concisa.",
            agent=self.target_agent
        )
        return temp_task.execute()  # 📌 Ejecutamos la tarea y obtenemos la respuesta
