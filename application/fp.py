class Monad:
    pass


class Maybe(Monad):
    pass


class Just(Maybe):
    def __init__(self, value):
        self.value = value


class Nothing(Maybe):
    def __init__(self, error_msg):
        self.error_msg = error_msg


def match(value, collection: dict) -> Maybe:
    return collection.get(value, Nothing)
