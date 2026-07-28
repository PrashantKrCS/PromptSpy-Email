import random

from agents.base_agent import BaseAgent
from models.email import Email


class ContentGenerationAgent(BaseAgent):
    """
    Generates a realistic business email using the selected
    persona and context.
    """

    RECIPIENTS = [
        "John Doe",
        "Alice Smith",
        "Robert Miller",
        "Priya Sharma",
        "Rahul Verma",
        "Kevin Wilson",
        "Anita Patel",
        "David Clark"
    ]

    def run(self, data):

        self.start()

        persona = data["persona"]
        context = data["context"]

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
                "description": "Instruction-like content detected (simulation only)"
            }
        )

        self.finish()

        return email

    def _generate_body(self, category, recipient, persona):

        templates = {

            "Meeting":
f"""Hi {recipient},

I hope you're doing well.

This is a reminder for our upcoming project kickoff meeting.

Agenda:
• Project overview
• Timeline
• Next steps

Please let me know if you have any questions.

Regards,

{persona.name}
{persona.title}
""",

            "Project":
f"""Hello {recipient},

The sprint planning session is scheduled for tomorrow.

We'll review the backlog, priorities, and deliverables for the next sprint.

Please come prepared with any blockers.

Thanks,

{persona.name}
""",

            "Finance":
f"""Hi {recipient},

Please find the updated invoice for this month's services.

Kindly review it and let me know if any clarification is required.

Thank you,

{persona.name}
Finance Team
""",

            "HR":
f"""Hello {recipient},

Your annual leave request has been approved.

Please coordinate with your manager before your planned leave dates.

Regards,

{persona.name}
HR Department
""",

            "Conference":
f"""Hi {recipient},

Attached is the latest speaker schedule for the conference.

Please review your assigned session timing and let us know if any updates are needed.

Regards,

{persona.name}
Conference Team
""",

            "Travel":
f"""Hello {recipient},

Your travel itinerary has been updated.

Please review the latest departure schedule before your journey.

Safe travels.

Regards,

{persona.name}
Travel Desk
""",

            "Support":
f"""Hi {recipient},

We're pleased to inform you that your support request has been resolved.

If you continue experiencing issues, please reply to this email.

Regards,

{persona.name}
Support Team
""",

            "Security":
f"""Hello {recipient},

This email confirms that your password has been successfully reset.

If you did not perform this action, please contact the Security Team immediately.

Regards,

{persona.name}
Security Team
""",

            "Procurement":
f"""Hi {recipient},

Your purchase order has been approved and forwarded for processing.

The procurement team will keep you updated on the delivery schedule.

Regards,

{persona.name}
Procurement Team
""",

            "Operations":
f"""Hello {recipient},

This is a reminder about the scheduled maintenance window this weekend.

Some internal services may be temporarily unavailable.

Thank you for your understanding.

Regards,

{persona.name}
Operations Team
""",

            "Customer Success":
f"""Hi {recipient},

We would like to schedule our Quarterly Business Review.

Please let us know your preferred availability for next week.

Looking forward to speaking with you.

Regards,

{persona.name}
Customer Success
""",

            "Marketing":
f"""Hello {recipient},

The monthly campaign performance report is now available.

Please review the attached summary before tomorrow's meeting.

Regards,

{persona.name}
Marketing Team
"""
        }

        return templates.get(
            category,
            f"""Hello {recipient},

This is an automated business communication.

Regards,

{persona.name}
"""
        )
