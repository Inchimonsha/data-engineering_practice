import psycopg2

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='mydb', user='postgres', password='123', host='localhost')

    cursor = conn.cursor()

    # Получаем список всех пользователей
    cursor.execute('SELECT * FROM weather')
    all_cities = cursor.fetchall()
    cursor.close()  # закрываем курсор
    conn.close()  # закрываем соединение
    print(all_cities)
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
