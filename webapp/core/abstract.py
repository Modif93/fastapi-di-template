from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Callable, Type

from dependency_injector import containers, providers
from sqlalchemy.orm import Session


class Repository(ABC):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self):
        pass

    def get_by_id(self, _id):
        pass
        
    def delete_by_id(self, _id):
        pass
    
class Service(ABC):
    def __init__(self, repository: Repository) -> None:
        self._repository: Repository = repository


def repository(target_repository:'Type[Repository]',session_factory):
    return providers.Factory(
        target_repository,
        session_factory=session_factory,
    )
    
def service(target_service:'Type[Service]',repository):
    return providers.Factory(
        target_service,
        repository=repository,
    )
