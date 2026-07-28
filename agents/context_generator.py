import random

from agents.base_agent import BaseAgent


class ContextGeneratorAgent(BaseAgent):
    """
    Generates a random business email scenario.
    """

    CONTEXTS = [

        {
            "category": "Meeting",
            "subject": "Project Kickoff Meeting",
            "summary": "Invite team members to the kickoff meeting.",
            "priority": "Normal"
        },

        {
            "category": "Project",
            "subject": "Sprint Planning Session",
            "summary": "Share sprint backlog and planning agenda.",
            "priority": "Normal"
        },

        {
            "category": "Finance",
            "subject": "Updated Invoice for July",
            "summary": "Send the revised invoice for approval.",
            "priority": "High"
        },

        {
            "category": "HR",
            "subject": "Annual Leave Approval",
            "summary": "Notify employee that leave has been approved.",
            "priority": "Normal"
        },

        {
            "category": "Conference",
            "subject": "Speaker Session Schedule",
            "summary": "Share conference agenda and speaker timings.",
            "priority": "Normal"
        },

        {
            "category": "Travel",
            "subject": "Flight Itinerary Updated",
            "summary": "Inform traveler about itinerary changes.",
            "priority": "High"
        },

        {
            "category": "Support",
            "subject": "Support Ticket Resolved",
            "summary": "Notify customer that their issue has been resolved.",
            "priority": "Normal"
        },

        {
            "category": "Security",
            "subject": "Password Reset Confirmation",
            "summary": "Confirm password reset request.",
            "priority": "High"
        },

        {
            "category": "Procurement",
            "subject": "Purchase Order Approved",
            "summary": "Purchase order has been approved for processing.",
            "priority": "Normal"
        },

        {
            "category": "Operations",
            "subject": "Scheduled Maintenance Notice",
            "summary": "Inform employees about upcoming maintenance.",
            "priority": "Low"
        },

        {
            "category": "Customer Success",
            "subject": "Quarterly Business Review",
            "summary": "Schedule a quarterly business review meeting.",
            "priority": "Normal"
        },

        {
            "category": "Marketing",
            "subject": "Campaign Performance Report",
            "summary": "Share monthly campaign performance metrics.",
            "priority": "Normal"
        }

    ]

    def run(self):

        self.start()

        context = random.choice(self.CONTEXTS)

        self.finish()

        return context
