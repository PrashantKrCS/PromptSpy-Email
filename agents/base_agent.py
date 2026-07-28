from abc import ABC
from abc import abstractmethod

from utils import banner
from utils import log


class BaseAgent(ABC):

    def __init__(self):

        self.name = self.__class__.__name__

    def start(self):

        banner(self.name)

        log("Starting agent...")

    def finish(self):

        log("Completed.")

    @abstractmethod
    def run(self, data):

        pass
