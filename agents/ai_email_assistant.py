from agents.base_agent import BaseAgent


class AIEmailAssistant(BaseAgent):

    """
    Simulates an AI assistant reading an email.

    It separates:

    • Visible content
    • Metadata
    • Simulation metadata

    without making any security decision.
    """

    def run(self, inbox):

        self.start()

        email = inbox["email"]

        result = {

            "message_id": inbox["message_id"],

            "sender": email.sender,

            "recipient": email.recipient,

            "subject": email.subject,

            "summary": self._summarize(email),

            "visible_text": {

                "body": email.body

            },

            "metadata": email.metadata,

            "simulation": email.simulation,

            "processing": {

                "visible_processed": True,

                "metadata_processed": True,

                "simulation_detected":
                    email.simulation.get("present", False)

            }

        }

        self.finish()

        return result

    def _summarize(self, email):

        category = email.metadata.get("category", "Business")

        summaries = {

            "Meeting":
                "Meeting invitation requiring attendee review.",

            "Finance":
                "Invoice notification received.",

            "HR":
                "HR notification received.",

            "Conference":
                "Conference schedule shared.",

            "Travel":
                "Travel itinerary updated.",

            "Support":
                "Support ticket update received.",

            "Security":
                "Security notification received.",

            "Project":
                "Project planning update received."

        }

        return summaries.get(
            category,
            "Business email processed."
        )
