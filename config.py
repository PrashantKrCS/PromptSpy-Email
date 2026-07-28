"""
Global configuration for the AI Email Simulation.
"""

APP_NAME = "AI Email Simulation"

VERSION = "1.0"

SIMULATION_DELAY = 1.0

LOG_LEVEL = "INFO"

SECURE_MODE = True

EMAIL_TEMPLATE = "templates/email_template.txt"

PROMPT_TEMPLATE = "templates/prompt_template.txt"

DEFAULT_PERSONA = {
    "name": "Sarah Johnson",
    "title": "Project Manager",
    "company": "Acme Technologies",
    "email": "sarah@example.com"
}
