#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from tfg_project.crew import TfgProyect

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
warnings.filterwarnings("ignore", category=DeprecationWarning)
topic ='Cual es el número de personas que hay el 01/11/2024 a las 8:50'

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
    }
    TfgProyect().crew().kickoff(inputs=inputs)
    