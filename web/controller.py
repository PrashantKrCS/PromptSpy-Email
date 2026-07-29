from pipeline import SimulationPipeline


class SimulationController:

    def __init__(self, secure_mode=True):

        self.secure_mode = secure_mode

    def execute(self):

        results = SimulationPipeline(
            self.secure_mode
        ).execute()

        email = results["email"]

        return {

            "persona": vars(results["persona"]),

            "context": results["context"],

            "email": {

                "sender": email.sender,

                "recipient": email.recipient,

                "subject": email.subject,

                "body": email.body,

                "metadata": email.metadata,

                "simulation": email.simulation

            },

            "assistant": results["assistant"],

            "trust": results["trust"],

            "reply": results["reply"]

        }
