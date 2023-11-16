"""Repositories module."""

from typing import Sequence, Type

from sqlalchemy import select

from ..core.abstract import Repository
from ..exception.entity import NotFoundError
from ..model.user import User


class UserRepository(Repository):

    def get_all(self) -> Sequence[User]:
        with self.session_factory() as session:
            return session.scalars(select(User)).all()

    def get_by_id(self, _id: int) -> Type[User]:
        with self.session_factory() as session:
            entity = session.get(User, _id)
            if not entity:
                raise UserNotFoundError(_id)

            return entity

    def add(self, email: str, password: str, is_active: bool = True) -> User:
        with self.session_factory() as session:
            user = User(email=email, hashed_password=password, is_active=is_active)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, _id: int) -> None:
        with self.session_factory() as session:
            entity = session.get(User, _id)
            if not entity:
                raise UserNotFoundError(_id)
            session.delete(entity)
            session.commit()


class UserNotFoundError(NotFoundError):
    entity_name: str = "User"
