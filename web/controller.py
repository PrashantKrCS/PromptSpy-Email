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

    # Generate sender persona
    persona = PersonaAgent().run()

    # Generate random email context
    context = ContextGeneratorAgent().run()

    # Generate email
    email = ContentGenerationAgent().run({
        "persona": persona,
        "context": context
    })

    # Deliver email
    inbox = EmailDeliveryAgent().run(email)

    # AI Assistant processes email
    parsed = AIEmailAssistant().run(inbox)

    # Trust Boundary simulation
    trust = IndirectPromptDemo().run(
        parsed,
        secure_mode=self.secure_mode
    )

    # Conversation simulation
    conversation = ConversationAgent().run(parsed)

    # AI reply generation
    reply = ReplyGenerationAgent().run(conversation)

    return {
        "persona": vars(persona),

        "context": context,

        "email": {
            "sender": email.sender,
            "recipient": email.recipient,
            "subject": email.subject,
            "body": email.body,
            "metadata": email.metadata,
            "simulation": email.simulation
        },

        "assistant": parsed,

        "trust": trust,

        "reply": reply
    }
