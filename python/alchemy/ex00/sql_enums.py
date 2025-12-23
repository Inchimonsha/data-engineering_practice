import enum


# class GenderEnum(str, enum.Enum):
class GenderEnum(enum.StrEnum):
    MALE = "мужчина"
    FEMALE = "женщина"


# class ProfessionEnum(str, enum.Enum):
class ProfessionEnum(enum.StrEnum):
    DEVELOPER = "разработчик"
    DESIGNER = "дизайнер"
    MANAGER = "менеджер"
    TEACHER = "учитель"
    DOCTOR = "врач"
    ENGINEER = "инженер"
    MARKETER = "маркетолог"
    WRITER = "писатель"
    ARTIST = "художник"
    LAWYER = "юрист"
    SCIENTIST = "ученый"
    NURSE = "медсестра"
    UNEMPLOYED = "безработный"


# class StatusPost(str, enum.Enum):
class StatusPost(enum.StrEnum):
    PUBLISHED = "опубликован"
    DELETED = "удален"
    UNDER_MODERATION = "на модерации"
    DRAFT = "черновик"
    SCHEDULED = "отложенная публикация"


# class RatingEnum(int, enum.Enum):
class RatingEnum(enum.IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
