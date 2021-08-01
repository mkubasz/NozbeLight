from application.command import Command
from application.command.create_task_command import CreateTaskCommand
from application.command_handler.task_command_handler import TaskCommandHandler
from application.fp import Maybe, Just, Nothing

bind = {
    CreateTaskCommand: Just(TaskCommandHandler())
}


def _get_command_handler(command_type) -> Maybe:
    return bind.get(command_type, Nothing)
