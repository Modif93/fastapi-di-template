"""Services module."""

from uuid import uuid4
from typing import Annotated, Iterator

from ..core.abstract import Service

from ..repository.user import UserRepository
from ..model.user import User


class UserService(Service):
    _repository: Annotated[UserRepository,"user_repository"]
    
    
    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self) -> User:
        uid = uuid4()
        return self._repository.add(email=f"{uid}@email.com", password="pwd")

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
