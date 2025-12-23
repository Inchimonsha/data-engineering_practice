import redis
import uuid

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# ===== Работа со строками (String) =====

def set_string(key, value):
    r.set(key, value)
    print(f"Строка установлена: {key} = {value}")

def get_string(key):
    value = r.get(key)
    print(f"Строка: {key} = {value}")
    return value

def delete_key(key):
    r.delete(key)
    print(f"Ключ удалён: {key}")

# ===== Работа с хэшами (Hash) =====

def add_new_user(username, password):
    user_id = str(uuid.uuid4())
    key = f"user:{user_id}"
    r.hset(key, mapping={
        "username": username,
        "password": password,
    })
    print(f"Добавлен пользователь: {username} с ключом {key}")
    return key

def get_user(user_key):
    user = r.hgetall(user_key)
    print(f"Пользователь {user_key}: {user}")
    return user

def update_user_password(user_key, new_password):
    r.hset(user_key, "password", new_password)
    print(f"Пароль пользователя {user_key} обновлён")

def delete_user(user_key):
    r.delete(user_key)
    print(f"Пользователь {user_key} удалён")

# ===== Работа со списками (List) =====

def add_list_items(key, *items):
    r.rpush(key, *items)
    print(f"Добавлены элементы в список {key}: {items}")

def get_list_items(key):
    items = r.lrange(key, 0, -1)
    print(f"Список {key}: {items}")
    return items

def pop_list_item_left(key):
    item = r.lpop(key)
    print(f"Извлечён элемент слева из списка {key}: {item}")
    return item

def pop_list_item_right(key):
    item = r.rpop(key)
    print(f"Извлечён элемент справа из списка {key}: {item}")
    return item

# ===== Работа с множествами (Set) =====

def add_set_members(key, *members):
    r.sadd(key, *members)
    print(f"Добавлены элементы в множество {key}: {members}")

def get_set_members(key):
    members = r.smembers(key)
    print(f"Множество {key}: {members}")
    return members

def remove_set_member(key, member):
    r.srem(key, member)
    print(f"Удалён элемент {member} из множества {key}")

# ===== Работа с отсортированными множествами (Sorted Set) =====

def add_zset_members(key, members_with_scores):
    """
    members_with_scores: dict вида {member: score}
    """
    r.zadd(key, members_with_scores)
    print(f"Добавлены элементы в отсортированное множество {key}: {members_with_scores}")

def get_zset_members(key, with_scores=True):
    members = r.zrange(key, 0, -1, withscores=with_scores)
    print(f"Отсортированное множество {key}: {members}")
    return members

def remove_zset_member(key, member):
    r.zrem(key, member)
    print(f"Удалён элемент {member} из отсортированного множества {key}")

# ===== Работа с общими операциями =====

def show_all_data():
    keys = r.keys('*')
    print("\nВсе ключи в Redis:", keys)

    for key in keys:
        key_type = r.type(key)
        print(f"\nКлюч: {key} | Тип: {key_type}")

        if key_type == 'string':
            value = r.get(key)
            print(f"Значение (string): {value}")

        elif key_type == 'hash':
            value = r.hgetall(key)
            print(f"Значение (hash): {value}")

        elif key_type == 'list':
            value = r.lrange(key, 0, -1)
            print(f"Значение (list): {value}")

        elif key_type == 'set':
            value = r.smembers(key)
            print(f"Значение (set): {value}")

        elif key_type == 'zset':
            value = r.zrange(key, 0, -1, withscores=True)
            print(f"Значение (zset): {value}")

        else:
            print("Неизвестный тип или пустое значение")

# ===== Пример использования =====

def main():
    # Строки
    set_string("site_name", "Example.com")
    get_string("site_name")

    # Хэши - пользователи
    user_key1 = add_new_user("alice", "password123")
    user_key2 = add_new_user("bob", "securepass")
    get_user(user_key1)
    update_user_password(user_key1, "newpassword")
    get_user(user_key1)

    # Списки
    add_list_items("tasks", "task1", "task2", "task3")
    get_list_items("tasks")
    pop_list_item_left("tasks")
    get_list_items("tasks")

    # Множества
    add_set_members("tags", "python", "redis", "database")
    get_set_members("tags")
    remove_set_member("tags", "redis")
    get_set_members("tags")

    # Отсортированные множества
    add_zset_members("leaderboard", {"alice": 100, "bob": 80, "carol": 120})
    get_zset_members("leaderboard")
    remove_zset_member("leaderboard", "bob")
    get_zset_members("leaderboard")

    # Продукты (хэш)
    product_key = f"product:{uuid.uuid4()}"
    r.hset(product_key, mapping={
        "name": "Hat",
        "price": "199.99",
        "count": "5",
    })

    show_all_data()


if __name__ == "__main__":
    main()
