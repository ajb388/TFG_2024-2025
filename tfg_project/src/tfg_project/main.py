#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from tfg_project.crew import TfgProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Cuáles son los edificios que tengo que visitar para llegar a la cafetería de humanidades desde las instalaciones deportivas?',
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'location': 'Universidad de Almeria',

    }
    
    try:
        TfgProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")