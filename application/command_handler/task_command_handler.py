from infrastucture.service.access_policy_service import AccessPolicyService, Permission
from application.command.create_task_command import CreateTaskCommand
from application.fp import Just, Maybe, Nothing
from domain.task.task import Task
from infrastucture.service.operation_service import OperationService
from infrastucture.service.subscription_service import SubscribeService


class TaskCommandHandler:
    def __init__(self):
        self.access_policy_service = AccessPolicyService()

    def dispatch(self, command_result: Maybe) -> Maybe:
        if isinstance(command_result, Nothing):
            return command_result
        if isinstance(command_result.value, CreateTaskCommand):
            return self._create_task(command_result.value, self.access_policy_service)
        return Just(())

    @staticmethod
    def _create_task(command: CreateTaskCommand, access_policy_service: AccessPolicyService) -> Maybe:
        aps = access_policy_service.check_perm(command, Permission.WRITE)
        if isinstance(aps, Nothing):
            return aps
        task_result = Task(command.name, command.description, command.author) \
            .create_task(SubscribeService(), OperationService()).app.commit()
        if isinstance(task_result, Nothing):
            return task_result
        return Just(())
