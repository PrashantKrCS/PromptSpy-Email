from agents.base_agent import BaseAgent


class ReplyGenerationAgent(BaseAgent):

    """
    Generates a simple AI-assisted reply.
    """

    def run(self, conversation, assistant_result):

        self.start()

        sender = assistant_result["sender"]

        if "<" in sender:
            sender = sender.split("<")[0].strip()

        reply = f"""Hi {sender},

Thank you for your email.

I've reviewed the information and will follow up shortly if any additional action is required.

Best regards,
AI Email Assistant
"""

        self.finish()

        return reply
