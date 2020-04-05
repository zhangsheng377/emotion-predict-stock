from abc import abstractmethod


class Senta():
    @abstractmethod
    def sentiments(self, doc):
        pass
