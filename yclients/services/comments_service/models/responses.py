from pydantic import Field
from ...common.models import DefaultResponse
from ._additional import Comment, RequestMeta

########################################################################################################################
# region Комментарии


class GetCommentsResponse(DefaultResponse):
    '''
    Модель ответа для получения комментариев.

    Аргументы:
    - data: Список комментариев.
    '''

    data: list[Comment] = Field(default=...)


class CreateCommentResponse(DefaultResponse):
    '''
    Модель ответа для создания нового комментария.

    Аргументы:
    - data: Данные созданного комментария.
    '''

    data: Comment = Field(default=...)


# endregion
