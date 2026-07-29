from agents.base_agent import BaseAgent
from models.conversation import Conversation


class ConversationAgent(BaseAgent):

    """
    Simulates an email conversation thread.
    """

    def run(self, assistant_result):

        self.start()

        conversation = Conversation()

        conversation.add(
            "Email",
            assistant_result["visible_text"]["body"]
        )

        conversation.add(
            "AI Summary",
            assistant_result["summary"]
        )

        self.finish()

        return conversation
