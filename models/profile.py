from dataclasses import dataclass


@dataclass
class Profile:

    name: str

    interests: list

    recent_event: str

    location: str

    def summary(self):

        return (
            f"{self.name} "
            f"attended {self.recent_event} "
            f"and is interested in "
            f"{', '.join(self.interests)}."
        )
