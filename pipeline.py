from agents.persona_agent import PersonaAgent
from agents.context_generator import ContextGeneratorAgent
from agents.content_generation_agent import ContentGenerationAgent

from agents.email_delivery_agent import EmailDeliveryAgent
from agents.ai_email_assistant import AIEmailAssistant
from agents.indirect_prompt_demo import IndirectPromptDemo
from agents.conversation_agent import ConversationAgent
from agents.reply_generation_agent import ReplyGenerationAgent


class SimulationPipeline:

    def __init__(self, secure_mode=True):

        self.secure_mode = secure_mode

    def execute(self):

        persona = PersonaAgent().run()

        context = ContextGeneratorAgent().run()

        email = ContentGenerationAgent().run(
            persona,
            context
        )

        inbox = EmailDeliveryAgent().run(email)

        assistant = AIEmailAssistant().run(inbox)

        trust = IndirectPromptDemo().run(
            assistant,
            secure_mode=self.secure_mode
        )

        conversation = ConversationAgent().run(
            assistant
        )

        reply = ReplyGenerationAgent().run(
            conversation,
            assistant,
            trust
        )

        return {

            "persona": persona,

            "context": context,

            "email": email,

            "inbox": inbox,

            "assistant": assistant,

            "trust": trust,

            "conversation": conversation,

            "reply": reply

        }
