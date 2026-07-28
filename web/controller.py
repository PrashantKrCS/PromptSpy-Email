from agents.persona_agent import PersonaAgent
from agents.profiling_agent import ProfilingAgent
from agents.pretext_agent import PretextAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.context_generator import ContextGeneratorAgent

from agents.email_delivery_agent import EmailDeliveryAgent
from agents.ai_email_assistant import AIEmailAssistant
from agents.conversation_agent import ConversationAgent
from agents.reply_generation_agent import ReplyGenerationAgent
from agents.indirect_prompt_demo import IndirectPromptDemo


class SimulationController:

    def __init__(self, secure_mode=True):

        self.secure_mode = secure_mode

    def execute(self):

      context = ContextGeneratorAgent().run()

        email = ContentGenerationAgent().run({
            "persona": persona,
            "context": context
        })

        inbox = EmailDeliveryAgent().run(email)

        parsed = AIEmailAssistant().run(inbox)

        trust = IndirectPromptDemo(
            secure_mode=self.secure_mode
        ).run(parsed)

        conversation = ConversationAgent().run(parsed)

        reply = ReplyGenerationAgent().run(conversation)

        return {
            "persona": vars(persona),
            "profile": vars(profile),
            "pretext": pretext,
            "email": {
                "sender": email.sender,
                "recipient": email.recipient,
                "subject": email.subject,
                "body": email.body,
                "metadata": email.metadata
            },
            "assistant": parsed,
            "trust": trust,
            "reply": reply
        }
