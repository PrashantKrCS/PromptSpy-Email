from agents.base_agent import BaseAgent
from utils import log


class EmailDeliveryAgent(BaseAgent):

    def run(self, email):

        self.start()

        inbox = {
            "folder": "Inbox",
            "status": "Delivered",
            "email": email
        }

        log("Email delivered to simulated inbox")

        self.finish()

        return inbox
