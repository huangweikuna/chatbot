from abc import abstractmethod


class Rule(object):
    @abstractmethod
    def predicate(self, msg) -> bool:
        pass

    @abstractmethod
    def call(self, msg):
        pass

    # The higher the value, the higher the priority
    def get_order(self) -> int:
        return 0

    def __str__(self):
        return str(self.get_order())