from asyncio import run

from sql_methods import add_user, create_user_example_4, get_user_by_id_example_3, get_users
from sql_enums import GenderEnum, ProfessionEnum


async def main():
    # await add_user("Алексей Яковенко", "alex@ya.ru", "12345")
    
    # users = await get_users()
    # for user in users.scalars():
    #     print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

    # user_profile = await get_user_by_id_example_3(
    #     username="john_doe",
    #     email="john.doe@example.com",
    #     password="password123",
    #     first_name="John",
    #     last_name="Doe",
    #     age=28,
    #     gender=GenderEnum.MALE,
    #     profession=ProfessionEnum.ENGINEER,
    #     interests=["hiking", "photography", "coding"],
    #     contacts={"phone": "+123456789", "email": "john.doe@example.com"},
    # )

    users = [
        {"username": "michael_brown", "email": "michael.brown@example.com", "password": "pass1234"},
        {"username": "sarah_wilson", "email": "sarah.wilson@example.com", "password": "mysecurepwd"},
        {"username": "david_clark", "email": "david.clark@example.com", "password": "davidsafe123"},
        {"username": "emma_walker", "email": "emma.walker@example.com", "password": "walker987"},
        {"username": "james_martin", "email": "james.martin@example.com", "password": "martinpass001"}
    ]

    await create_user_example_4(users_data=users)


if __name__ == "__main__":
    run(main())
