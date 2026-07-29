from dataclasses import dataclass, field

from typing import List


@dataclass
class Conversation:

    messages: List = field(default_factory=list)

    def add(self, role, content):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )
