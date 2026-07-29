import random

from agents.base_agent import BaseAgent


class ContextGeneratorAgent(BaseAgent):

    CONTEXTS = [

        {
            "category": "Meeting",
            "subject": "Project Kickoff Meeting",
            "priority": "Normal"
        },

        {
            "category": "Finance",
            "subject": "Updated Invoice",
            "priority": "High"
        },

        {
            "category": "HR",
            "subject": "Annual Leave Approval",
            "priority": "Normal"
        },

        {
            "category": "Conference",
            "subject": "Speaker Schedule",
            "priority": "Normal"
        },

        {
            "category": "Travel",
            "subject": "Flight Itinerary Updated",
            "priority": "High"
        },

        {
            "category": "Support",
            "subject": "Support Ticket Resolved",
            "priority": "Normal"
        },

        {
            "category": "Security",
            "subject": "Password Reset Confirmation",
            "priority": "High"
        },

        {
            "category": "Project",
            "subject": "Sprint Planning Session",
            "priority": "Normal"
        }

    ]

    def run(self):

        self.start()

        context = random.choice(self.CONTEXTS)

        self.finish()

        return context
