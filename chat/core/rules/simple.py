from chat.core.rule import Rule


class SimpleRule(Rule):
    def predicate(self, msg) -> bool:
        return True

    def call(self, msg):
        pass

    def get_order(self) -> int:
        return 1

