from agents.base_agent import BaseAgent


class ReplyGenerationAgent(BaseAgent):

    """
    Generates a human review and an AI assistant response.
    """

    def run(self, conversation, assistant_result, trust_result):

        self.start()

        sender = assistant_result["sender"]

        if "<" in sender:
            sender = sender.split("<")[0].strip()

        # Human response is always based on the visible email content.
        human_reply = f"""Hi {sender},

Thank you for your email.

I've reviewed the information in your message and will follow up shortly if any additional action is required.

Best regards,
Human Reviewer
"""

        # AI response varies depending on the trust-boundary outcome.
        if trust_result["processing_state"] == "isolated":

            ai_reply = f"""Hi {sender},

I've summarized the visible email content and prepared this response.

Simulation metadata was detected and excluded from downstream processing.

Best regards,
AI Email Assistant
"""

        else:

            ai_reply = f"""Hi {sender},

This run is operating in Demonstration Mode.

The simulation illustrates how a naïve AI pipeline could allow instruction-like content to influence downstream reasoning when trust boundaries are not enforced.

No automated action has been taken—this response is provided for educational purposes only.

Best regards,
AI Email Assistant
"""

        self.finish()

        return {
            "human_reply": human_reply,
            "ai_reply": ai_reply
        }
