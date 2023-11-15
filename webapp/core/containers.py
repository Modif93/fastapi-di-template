"""Containers module."""

from dependency_injector import containers, providers

from .abstract import service,repository
from .database import Database

from ..repository.user import UserRepository
from ..service.user import UserService

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["..endpoint.user"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = repository(UserRepository,db.provided.session)
    
    user_service = service(UserService,user_repository)
