from utils import divider
from utils import log


class BaseAgent:

    name = "BaseAgent"

    def start(self):

        divider(self.__class__.__name__)

        log("Starting agent...")

    def finish(self):

        log("Completed.")
