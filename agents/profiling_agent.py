from agents.base_agent import BaseAgent
from models.profile import Profile
from utils import log


class ProfilingAgent(BaseAgent):

    def run(self, data=None):

        self.start()

        profile = Profile(
            name="John Doe",
            interests=[
                "AI",
                "Cyber Security",
                "Cloud"
            ],
            recent_event="AI Security Summit",
            location="New York"
        )

        log("Loaded fictional recipient profile")

        self.finish()

        return profile
