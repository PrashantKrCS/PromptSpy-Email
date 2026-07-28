from agents.base_agent import BaseAgent
from utils import log


class AIEmailAssistant(BaseAgent):

    def run(self, inbox):

        self.start()

        email = inbox["email"]

        parsed = {
            "visible_text": email.body,
            "metadata": email.metadata,
            "subject": email.subject,
            "sender": email.sender
        }

        log("Parsed email")
        log("Extracted visible content")
        log("Extracted metadata")

        self.finish()

        return parsed
