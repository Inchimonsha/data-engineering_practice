import random
from faker import Faker
import pandas as pd

fake = Faker()

# Генерация данных для таблицы typeActivity
type_activity_data = []
for i in range(1, 6):
    type_activity_data.append({
        "id": i,
        "name": fake.word().capitalize()
    })

# Генерация данных для таблицы bell
bell_data = []
for i in range(1, 11):
    start_time = fake.time()
    finish_time = fake.time()
    bell_data.append({
        "id": i,
        "tStart": start_time,
        "tFinish": finish_time
    })

# Генерация данных для таблицы discipline
discipline_data = []
for i in range(1, 21):
    discipline_data.append({
        "id": i,
        "name": fake.catch_phrase()
    })

# Генерация данных для таблицы lecturer
lecturer_data = []
for i in range(1, 21):
    lecturer_data.append({
        "id": i,
        "fullName": fake.name(),
        "phoneNumber": fake.phone_number(),
        "id_institute": random.randint(1, 5)
    })

# Генерация данных для таблицы schedule
schedule_data = []
for i in range(1, 6):
    schedule_data.append({
        "id": i,
        "nameSemester": fake.word().capitalize()
    })

# Генерация данных для таблицы classroom
classroom_data = []
for i in range(1, 21):
    classroom_data.append({
        "id": i,
        "name": random.randint(1, 100),
        "capacity": random.randint(20, 100)
    })

# Генерация данных для таблицы weekday
weekday_data = []
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(1, 8):
    weekday_data.append({
        "id": i,
        "name": weekdays[i-1]
    })

# Генерация данных для таблицы class_
class_data = []
for i in range(1, 51):
    class_data.append({
        "id": i,
        "numberClass": random.randint(1, 10),
        "id_typeActivity": random.randint(1, 5),
        "id_bell": random.randint(1, 10),
        "id_discipline": random.randint(1, 20),
        "id_lecturer": random.randint(1, 20),
        "id_schedule": random.randint(1, 5),
        "id_classroom": random.randint(1, 20),
        "id_weekday": random.randint(1, 7)
    })

# Преобразование данных в DataFrame для удобного просмотра
dataframes = {
    "typeActivity": pd.DataFrame(type_activity_data),
    "bell": pd.DataFrame(bell_data),
    "discipline": pd.DataFrame(discipline_data),
    "lecturer": pd.DataFrame(lecturer_data),
    "schedule": pd.DataFrame(schedule_data),
    "classroom": pd.DataFrame(classroom_data),
    "weekday": pd.DataFrame(weekday_data),
    "class_": pd.DataFrame(class_data)
}

# Вывод данных
for table_name, df in dataframes.items():
    print(f"\nTable: {table_name}")
    print(df)
