from datetime import datetime
import uuid

from agents.base_agent import BaseAgent


class EmailDeliveryAgent(BaseAgent):

    def run(self, email):

        self.start()

        inbox = {
            "message_id": str(uuid.uuid4())[:8],
            "folder": "Inbox",
            "status": "Delivered",
            "received_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "email": email
        }

        self.finish()

        return inbox
