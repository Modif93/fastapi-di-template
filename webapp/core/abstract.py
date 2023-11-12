from dependency_injector import containers, providers
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session

class Repository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory
        
    
class Service:
    def __init__(self, repository: Repository) -> None:
        self._repository: Repository = repository


def repository(target_repository:Repository,session_factory):
    return providers.Factory(
        target_repository,
        session_factory=session_factory,
    )
    
def service(target_service:Service,repository):
    return providers.Factory(
        target_service,
        repository=repository,
    )
