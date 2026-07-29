class Email:

    def __init__(
        self,
        sender,
        recipient,
        subject,
        body,
        metadata=None,
        simulation=None
    ):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.metadata = metadata or {}
        self.simulation = simulation or {}
