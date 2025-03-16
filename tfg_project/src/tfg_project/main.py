#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from tfg_project.crew import TfgProyect

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
topic ='Qué cafeterías hay en el campus?'

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
    }
    
    try:
        TfgProyect().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': topic,
    }
    try:
        TfgProyect().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TfgProyect().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': topic,
    }
    try:
        TfgProyect().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
