from agents.base_agent import BaseAgent
from models.persona import Persona
from config import DEFAULT_PERSONA
from utils import log


class PersonaAgent(BaseAgent):

    def run(self, data=None):

        self.start()

        persona = Persona(
            name=DEFAULT_PERSONA["name"],
            title=DEFAULT_PERSONA["title"],
            company=DEFAULT_PERSONA["company"],
            email=DEFAULT_PERSONA["email"]
        )

        log("Generated fictional sender persona")

        self.finish()

        return persona
