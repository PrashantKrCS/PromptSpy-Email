from agents.base_agent import BaseAgent


class AIEmailAssistant(BaseAgent):
    """
    Simulates how an AI email assistant processes an incoming email.

    Responsibilities:
    - Read visible email content
    - Extract metadata
    - Preserve simulation metadata
    - Prepare structured data for the Trust Boundary demo
    """

    def run(self, email):

        self.start()

        assistant_result = {
            "sender": email.sender,
            "recipient": email.recipient,
            "subject": email.subject,

            "visible_text": {
                "body": email.body
            },

            "metadata": email.metadata,

            "simulation": email.simulation,

            "processing": {
                "visible_content_processed": True,
                "metadata_processed": True,
                "simulation_detected": email.simulation.get(
                    "present",
                    False
                )
            },

            "summary": self._summarize(email)
        }

        self.finish()

        return assistant_result

    def _summarize(self, email):

        category = email.metadata.get(
            "category",
            "General"
        )

        summaries = {

            "Meeting":
                "Meeting invitation received requiring attendee review.",

            "Project":
                "Project planning update requiring team attention.",

            "Finance":
                "Finance-related communication regarding an invoice.",

            "HR":
                "Human Resources notification received.",

            "Conference":
                "Conference schedule shared with participants.",

            "Travel":
                "Travel itinerary update requiring confirmation.",

            "Support":
                "Support ticket resolution notification received.",

            "Security":
                "Security-related notification received.",

            "Procurement":
                "Purchase order approval notification received.",

            "Operations":
                "Operational maintenance notification received.",

            "Customer Success":
                "Customer meeting invitation received.",

            "Marketing":
                "Marketing performance report shared."
        }

        return summaries.get(
            category,
            "Business email processed successfully."
        )
