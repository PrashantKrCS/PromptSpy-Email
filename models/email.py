from dataclasses import dataclass, field


@dataclass
class Email:

    sender: str

    recipient: str

    subject: str

    body: str

    metadata: dict = field(default_factory=dict)

    def render(self):

        return f"""
FROM    : {self.sender}

TO      : {self.recipient}

SUBJECT : {self.subject}

--------------------------------------------------

{self.body}
"""
