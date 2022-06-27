from chat.core.rule import Rule


class HelpRule(Rule):

    def predicate(self, msg) -> bool:
        return msg == "help"

    def call(self, msg):
        return "help !!!!!!!!!!!"

    def get_order(self) -> int:
        return 99
