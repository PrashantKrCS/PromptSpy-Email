from agents.base_agent import BaseAgent
from models.email import Email
from utils import log


class ContentGenerationAgent(BaseAgent):

    def run(self, data):

        self.start()

        persona = data["persona"]
        profile = data["profile"]
        pretext = data["pretext"]

        body = f"""
Hi {profile.name},

{pretext}

It was great seeing your interest in AI and cloud security.

Would you be available sometime this week to discuss ideas from the event?

Best regards,

{persona.name}
{persona.title}
{persona.company}
"""

        email = Email(
            sender=persona.email,
            recipient=f"{profile.name.lower().replace(' ','')}@example.com",
            subject="Following up after AI Security Summit",
            body=body,
            metadata={
                "priority": "normal",
                "classification": "business",
                "simulation": True
            }
        )

        log("Generated email")

        self.finish()

        return email
