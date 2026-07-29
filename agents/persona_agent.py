import random

from agents.base_agent import BaseAgent
from models.persona import Persona


class PersonaAgent(BaseAgent):

    PERSONAS = [

        Persona(
            "Sarah Johnson",
            "Project Manager",
            "Acme Technologies",
            "sarah.johnson@acmetech.demo"
        ),

        Persona(
            "Emily Davis",
            "HR Manager",
            "PeopleFirst HR",
            "emily.davis@peoplefirst.demo"
        ),

        Persona(
            "Michael Brown",
            "Finance Lead",
            "FinEdge Solutions",
            "michael.brown@finedge.demo"
        ),

        Persona(
            "Daniel Wilson",
            "IT Administrator",
            "CloudOps Systems",
            "daniel.wilson@cloudops.demo"
        ),

        Persona(
            "Sophia Miller",
            "Travel Coordinator",
            "SkyRoute Travel",
            "sophia.miller@skyroute.demo"
        ),

        Persona(
            "James Anderson",
            "Customer Success Manager",
            "Nova Software",
            "james.anderson@novasoftware.demo"
        )

    ]

    def run(self):

        self.start()

        persona = random.choice(self.PERSONAS)

        self.finish()

        return persona
