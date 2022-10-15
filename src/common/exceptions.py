from typing import Any


class CommonException(Exception):
    """Base exception class for all exceptions in this project."""

    code: int = 500
    message: str = 'An unknown error occurred.'
    detail: Any | None

    def __init__(
        self, code: int | None = None, message: str | None = None, detail: Any | None = None
    ):
        self.code = code or self.code
        self.message = message or self.message
        self.detail = detail

    def __str__(self):
        return f'{self.code}: {self.message}'

    def to_dict(self):
        '''
        Convert the exception to a dictionary response.
        '''
        return {
            'code': self.code,
            'message': self.message,
            'detail': self.detail,
        }
