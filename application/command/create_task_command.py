from application.command import Command
from application.fp import Maybe, Just, Nothing


class CreateTaskCommand(Command):
    def __init__(self, name, description, author):
        self.name = name
        self.description = description
        self.author = author

    def validate(self) -> Maybe:
        if self.name and self.description and self.author:
            return Just(self)
        return Nothing("Invalid model")
