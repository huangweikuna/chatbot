from chat.core.rule import Rule


class DefaultRule(Rule):
    def predicate(self, msg) -> bool:
        return True

    def call(self, msg):
        return "default"

    def get_order(self) -> int:
        return -1
