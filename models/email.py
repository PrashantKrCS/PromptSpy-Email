from dataclasses import dataclass, field

from typing import Dict


@dataclass
class Email:

    sender: str

    recipient: str

    subject: str

    body: str

    metadata: Dict = field(default_factory=dict)

    simulation: Dict = field(default_factory=dict)

    def render(self):

        return f"""
From: {self.sender}
To: {self.recipient}
Subject: {self.subject}

{self.body}
"""
