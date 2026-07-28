from agents.base_agent import BaseAgent
from utils import log


class PretextAgent(BaseAgent):

    def run(self, data):

        self.start()

        persona = data["persona"]
        profile = data["profile"]

        pretext = (
            f"{persona.name} recently noticed "
            f"{profile.name} participated in "
            f"{profile.recent_event}."
        )

        log("Generated personalized pretext")

        self.finish()

        return pretext
