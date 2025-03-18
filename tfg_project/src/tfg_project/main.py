#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from tfg_project.crew import TfgProyect

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
topic ='dame los datos de la personas'

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
    }
    TfgProyect().crew().kickoff(inputs=inputs)
    