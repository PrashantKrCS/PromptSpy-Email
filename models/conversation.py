from dataclasses import dataclass, field


@dataclass
class Conversation:

    history: list = field(default_factory=list)

    def add(self, speaker, message):

        self.history.append({
            "speaker": speaker,
            "message": message
        })

    def show(self):

        for item in self.history:

            print(
                f"{item['speaker']}: {item['message']}"
            )
