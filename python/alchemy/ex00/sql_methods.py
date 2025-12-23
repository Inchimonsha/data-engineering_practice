from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import connection
from models import Profile, User
from sql_enums import GenderEnum, ProfessionEnum


@connection
async def get_users(session: AsyncSession):
    return await session.execute(select(User))


@connection
async def add_user(username: str, email: str, password: str, session: AsyncSession):
    """
    Создает нового пользователя с использованием ORM SQLAlchemy.

    Аргументы:
    - username: str - имя пользователя
    - email: str - адрес электронной почты
    - password: str - пароль пользователя
    - session: AsyncSession - асинхронная сессия базы данных

    Возвращает:
    - int - идентификатор созданного пользователя
    """
    # Создаём объект User (инстанс модели)
    new_user = User(username=username, email=email, password=password)
    # Добавляем объект в сессию
    session.add(new_user)
    # Сохраняем изменения в базе данных
    await session.commit()
    return new_user.id


@connection
async def get_user_by_id_example_2(username: str, email: str, password: str,
                                   first_name: str,
                                   last_name: str | None,
                                   age: str | None,
                                   gender: GenderEnum,
                                   profession: ProfessionEnum | None,
                                   interests: list | None,
                                   contacts: dict | None,
                                   session: AsyncSession) -> dict[str, int]:
    user = User(username=username, email=email, password=password)
    session.add(user)
    await session.commit()

    profile = Profile(
        user_id=user.id,
        first_name=first_name,
        last_name=last_name,
        age=age,
        gender=gender,
        profession=profession,
        interests=interests,
        contacts=contacts)

    session.add(profile)
    await session.commit()
    print(f'Создан пользователь с ID {user.id} и ему присвоен профиль с ID {profile.id}')
    return {'user_id': user.id, 'profile_id': profile.id}


@connection
async def get_user_by_id_example_3(username: str, email: str, password: str,
                                   first_name: str,
                                   last_name: str | None,
                                   age: str | None,
                                   gender: GenderEnum,
                                   profession: ProfessionEnum | None,
                                   interests: list | None,
                                   contacts: dict | None,
                                   session: AsyncSession) -> dict[str, int]:
    try:
        user = User(username=username, email=email, password=password)
        session.add(user)
        await session.flush()  # Промежуточный шаг для получения user.id без коммита

        profile = Profile(
            user_id=user.id,
            first_name=first_name,
            last_name=last_name,
            age=age,
            gender=gender,
            profession=profession,
            interests=interests,
            contacts=contacts
        )
        session.add(profile)

        # Один коммит для обоих действий
        await session.commit()

        print(f'Создан пользователь с ID {user.id} и ему присвоен профиль с ID {profile.id}')
        return {'user_id': user.id, 'profile_id': profile.id}

    except Exception as e:
        await session.rollback()  # Откатываем транзакцию при ошибке
        raise e


@connection
async def create_user_example_4(users_data: list[dict], session: AsyncSession) -> list[int]:
    """
    Создает нескольких пользователей с использованием ORM SQLAlchemy.

    Аргументы:
    - users_data: list[dict] - список словарей, содержащих данные пользователей
      Каждый словарь должен содержать ключи: 'username', 'email', 'password'.
    - session: AsyncSession - асинхронная сессия базы данных

    Возвращает:
    - list[int] - список идентификаторов созданных пользователей
    """
    users_list = [
        User(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        for user_data in users_data
    ]
    session.add_all(users_list)
    await session.commit()
    return [user.id for user in users_list]
