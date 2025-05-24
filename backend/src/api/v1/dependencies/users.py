from services.users import UsersService
from repositories.users import UsersRepository


def users_service():
    return UsersService(UsersRepository)