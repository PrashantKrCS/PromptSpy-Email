"""
AI Email Simulation
Main Entry Point
"""

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

from web.app import create_app

import argparse


def run_pipeline(secure_mode=True):
    """
    Execute the complete simulation pipeline.
    """

    print("=" * 70)
    print("AI EMAIL SECURITY SIMULATION")
    print("=" * 70)

    # ------------------------
    # Persona Agent
    # ------------------------

    persona = PersonaAgent().run()

    # ------------------------
    # Profiling Agent
    # ------------------------

    #profile = ProfilingAgent().run()

    # ------------------------
    # Pretext Agent
    # ------------------------

    context = ContextGeneratorAgent().run()
    
   # pretext = PretextAgent().run({
     #   "persona": persona,
      #  "profile": profile
    #})

    # ------------------------
    # Email Generation
    # ------------------------

    email = ContentGenerationAgent().run({
        "persona": persona,
        "context" : context
    })

    # Example metadata for demonstration purposes
    email.metadata = {
        "priority": "normal",
        "classification": "business",
        "simulation": True
    }

    # ------------------------
    # Delivery
    # ------------------------

    inbox = EmailDeliveryAgent().run(email)

    # ------------------------
    # AI Assistant
    # ------------------------

    parsed = AIEmailAssistant().run(inbox)

    # ------------------------
    # Trust Boundary Demo
    # ------------------------

    trust_result = IndirectPromptDemo(
        secure_mode=secure_mode
    ).run(parsed)

    # ------------------------
    # Conversation
    # ------------------------

    conversation = ConversationAgent().run(parsed)

    # ------------------------
    # Reply
    # ------------------------

    reply = ReplyGenerationAgent().run(conversation)

    return {
        "persona": persona,
        "profile": profile,
        "pretext": pretext,
        "email": email,
        "parsed_email": parsed,
        "trust_boundary": trust_result,
        "conversation": conversation,
        "reply": reply
    }


def start_console():

    print("\nRunning Console Simulation...\n")

    results = run_pipeline(
        secure_mode=True
    )

    print("\n")
    print("=" * 70)
    print("FINAL EMAIL")
    print("=" * 70)

    print(results["email"].render())

    print("\n")
    print("=" * 70)
    print("GENERATED REPLY")
    print("=" * 70)

    print(results["reply"])


def start_web():

    print("Starting Flask Dashboard...")

    app = create_app()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        choices=[
            "console",
            "web"
        ],
        default="console"
    )

    args = parser.parse_args()

    if args.mode == "console":

        start_console()

    else:

        start_web()
