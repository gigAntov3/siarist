from utils.repository import SQLAlchemyRepository

from models.users import UserModel


class UsersRepository(SQLAlchemyRepository):
    model = UserModel