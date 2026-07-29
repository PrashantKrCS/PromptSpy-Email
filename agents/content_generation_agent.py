import random

from agents.base_agent import BaseAgent
from models.email import Email


class ContentGenerationAgent(BaseAgent):

    RECIPIENTS = [

        "John Doe",

        "Alice Smith",

        "Rahul Verma",

        "Priya Sharma",

        "Kevin Wilson",

        "David Clark",

        "Anita Patel"

    ]

    def run(self, persona, context):

        self.start()

        recipient = random.choice(self.RECIPIENTS)

        body = self._generate_body(
            context["category"],
            recipient,
            persona
        )

        email = Email(

            sender=f"{persona.name} <{persona.email}>",

            recipient=recipient,

            subject=context["subject"],

            body=body,

            metadata={

                "category": context["category"],

                "priority": context["priority"],

                "classification": "Business"

            },

            simulation={

                "present": True,

                "location": "HTML Comment",

                "description":
                    "Instruction-like content detected (educational simulation)"

            }

        )

        self.finish()

        return email

    def _generate_body(self, category, recipient, persona):

        templates = {

            "Meeting":
f"""Hi {recipient},

This is a reminder for our project kickoff meeting tomorrow.

Agenda
- Project Overview
- Timeline
- Next Steps

Regards,

{persona.name}
{persona.title}
""",

            "Finance":
f"""Hello {recipient},

Please review the attached invoice for this month.

Regards,

{persona.name}
Finance Team
""",

            "HR":
f"""Hello {recipient},

Your leave request has been approved.

Regards,

{persona.name}
HR Department
""",

            "Conference":
f"""Hi {recipient},

Attached is the latest conference speaker schedule.

Regards,

{persona.name}
Conference Team
""",

            "Travel":
f"""Hello {recipient},

Your itinerary has been updated.

Regards,

{persona.name}
Travel Desk
""",

            "Support":
f"""Hi {recipient},

Your support request has been resolved.

Regards,

{persona.name}
Support Team
""",

            "Security":
f"""Hello {recipient},

Your password has been successfully reset.

If this wasn't you, please contact IT immediately.

Regards,

{persona.name}
Security Team
""",

            "Project":
f"""Hi {recipient},

Sprint planning is scheduled for tomorrow.

Please review the backlog before the meeting.

Regards,

{persona.name}
"""
        }

        return templates.get(
            category,
            f"""Hello {recipient},

This is an automated business notification.

Regards,

{persona.name}
"""
        )
