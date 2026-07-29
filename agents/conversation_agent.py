from agents.base_agent import BaseAgent
from models.conversation import Conversation
from utils import log


class ConversationAgent(BaseAgent):

    def run(self, parsed_email):

        self.start()

        conversation = Conversation()

        conversation.add(
            "Email",
            parsed_email["visible_text"]["body"]
        )

        log("Conversation context created")

        self.finish()

        return conversation
