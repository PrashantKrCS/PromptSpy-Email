from agents.base_agent import BaseAgent
from utils import log


class IndirectPromptDemo(BaseAgent):

    def __init__(self, secure_mode=True):
        super().__init__()
        self.secure_mode = secure_mode

    def run(self, parsed_email):

        self.start()

        visible = parsed_email["visible_text"]
        metadata = parsed_email["metadata"]

        print("\n========== Visible Content ==========\n")
        print(visible)

        print("\n========== Metadata ==========\n")
        print(metadata)

        if self.secure_mode:

            decision = {
                "mode": "Secure",
                "trusted_input": visible,
                "untrusted_input": metadata,
                "action": "Metadata kept separate from user-visible content."
            }

            log("Trust boundary enforced")

        else:

            decision = {
                "mode": "Demo (Naïve)",
                "combined_context": {
                    "visible": visible,
                    "metadata": metadata
                },
                "action": (
                    "Illustration only: visible content and metadata "
                    "are combined before reasoning."
                )
            }

            log("Trust boundary not enforced (simulation)")

        self.finish()

        return decision
