"""Repositories module."""

from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from ..core.abstract import Repository
from ..exception.entity import NotFoundError
from ..model.user import User


class UserRepository(Repository):

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, _id: int) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter_by(id=_id).first()
            if not user:
                raise UserNotFoundError(_id)
            return user

    def add(self, email: str, password: str, is_active: bool = True) -> User:
        with self.session_factory() as session:
            user = User(email=email, hashed_password=password, is_active=is_active)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, _id: int) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter_by(id=_id).first()
            if not entity:
                raise UserNotFoundError(_id)
            session.delete(entity)
            session.commit()

class UserNotFoundError(NotFoundError):

    entity_name: str = "User"
