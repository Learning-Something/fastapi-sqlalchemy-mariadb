from common.exceptions import CommonException


class TodoNotFound(CommonException):
    def __init__(self, todo_id: int):
        super().__init__(
            code=404,
            message=f'Todo with id {todo_id} not found',
        )
