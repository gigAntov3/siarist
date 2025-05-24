from fastapi import APIRouter, Depends, Query

from typing import Annotated

from schemas.users import (
    UserSchema,
    AnswerUserSchema,
    UserAddSchema,
    AnswerUserAddSchema,
    AnswerUsersSchema,
)

from services.users import UsersService

from api.v1.dependencies.users import users_service


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("")
async def get_users(
    users_service: Annotated[UsersService, Depends(users_service)],
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
) -> AnswerUsersSchema:
    users = await users_service.get_users(limit=limit, offset=offset)
    return AnswerUsersSchema(ok=True, message="Users retrieved successfully", users=users)


@router.post("")
async def add_user(
    user: UserAddSchema,
    users_service: Annotated[UsersService, Depends(users_service)],
) -> AnswerUserAddSchema:
    user_id = await users_service.add_user(user)
    return AnswerUserAddSchema(ok=True, message="User added successfully", user_id=user_id)


@router.get("/{user_id}")
async def get_user(
    user_id: int,
    users_service: Annotated[UsersService, Depends(users_service)],
) -> AnswerUserSchema:
    user = await users_service.get_user(user_id)
    return AnswerUserSchema(ok=True, message="User retrieved successfully", user=user)