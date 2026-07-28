from agents.base_agent import BaseAgent


class IndirectPromptDemo(BaseAgent):
    """
    Educational simulation of how an AI system handles
    instruction-like content embedded in an email.

    Modes
    -----
    Demonstration
        Simulates a naïve implementation where instruction-like
        content is treated as part of the input.

    Secure
        Simulates a protected implementation where instruction-like
        content is isolated from visible email content.
    """

    def run(self, assistant_result, secure_mode=True):

        self.start()

        simulation = assistant_result.get("simulation", {})
        processing = assistant_result.get("processing", {})

        simulation_present = simulation.get("present", False)

        if secure_mode:

            result = {
                "mode": "Secure",

                "status": "Protected",

                "decision":
                    "Instruction-like content isolated before AI processing.",

                "reason":
                    "Visible email content processed independently from simulation metadata.",

                "actions": [
                    "Read visible email",
                    "Read metadata",
                    "Detected simulation metadata",
                    "Excluded simulation layer",
                    "Generated summary from visible content only"
                ],

                "simulation_detected": simulation_present,

                "processing": processing
            }

        else:

            result = {
                "mode": "Demonstration",

                "status": "Naïve Pipeline",

                "decision":
                    "Simulation demonstrates how instruction-like content could influence downstream reasoning if not isolated.",

                "reason":
                    "No trust-boundary separation between visible content and embedded metadata.",

                "actions": [
                    "Read visible email",
                    "Read metadata",
                    "Simulation metadata observed",
                    "No isolation applied",
                    "Generated output using all available information (simulation)"
                ],

                "simulation_detected": simulation_present,

                "processing": processing
            }

        self.finish()

        return result
