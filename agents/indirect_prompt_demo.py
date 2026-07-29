from agents.base_agent import BaseAgent


class IndirectPromptDemo(BaseAgent):

    """
    Demonstrates trust-boundary handling.

    No executable prompt injection is performed.

    This module only visualizes how an AI pipeline
    could distinguish between visible email content
    and instruction-like metadata in an educational
    simulation.
    """

    def run(self, assistant_result, secure_mode=True):

        self.start()

        detected = assistant_result["simulation"].get(
            "present",
            False
        )

        if secure_mode:

            decision = {

                "mode": "Secure",

                "status": "Protected",

                "decision":
                    "Instruction-like content isolated before summarization.",

                "reason":
                    "Only visible email content contributed to the summary.",

                "simulation_detected": detected,

                "timeline": [

                    "Read email",

                    "Extract visible content",

                    "Read metadata",

                    "Simulation metadata identified",

                    "Simulation layer excluded",

                    "Summary generated"

                ]

            }

        else:

            decision = {

                "mode": "Demonstration",

                "status": "Naive Pipeline",

                "decision":
                    "Simulation illustrates how instruction-like content could influence downstream processing if trust boundaries are absent.",

                "reason":
                    "Educational visualization only.",

                "simulation_detected": detected,

                "timeline": [

                    "Read email",

                    "Read metadata",

                    "Simulation metadata observed",

                    "No isolation applied",

                    "Summary generated"

                ]

            }

        self.finish()

        return decision
