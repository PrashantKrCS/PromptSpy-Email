from agents.base_agent import BaseAgent
from utils import log


class ReplyGenerationAgent(BaseAgent):

    def run(self, conversation):

        self.start()

        reply = """
Hi Sarah,

Thank you for your email.

I'd be happy to schedule some time next week.

Regards,

John
"""

        conversation.add(
            "Assistant",
            reply
        )

        log("Reply generated")

        self.finish()

        return reply
