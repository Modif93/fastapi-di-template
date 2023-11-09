"""Containers module."""

from dependency_injector import containers, providers

from .database import Database
from ..repository.user import UserRepository
from ..service.user import UserService

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["..endpoint.user"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
