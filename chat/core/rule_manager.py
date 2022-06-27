from chat.core.rule import Rule


class RuleManager(object):
    def __init__(self):
        self.rules = []
        self._registration()

    def _registration(self):
        try:
            import chat.core.rules
        except ImportError as exc:
            raise ImportError("import error") from exc
        for rule in Rule.__subclasses__():
            self.rules.append(rule())
        self.rules.sort(key=lambda r: r.get_order(), reverse=True)

    def call(self, msg):
        for rule in self.rules:
            if rule.predicate(msg):
                rule.call(msg)
                break


manage = RuleManager()
