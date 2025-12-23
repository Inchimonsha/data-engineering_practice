import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Загружаем набор данных
iris = load_iris()
X = iris.data
y = iris.target

# Делим данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Параметр модели
C_param = 1.0

# Начинаем трекинг эксперимента
with mlflow.start_run():
    # Обучаем модель
    model = LogisticRegression(C=C_param, max_iter=200)
    model.fit(X_train, y_train)

    # Предсказываем
    preds = model.predict(X_test)

    # Оцениваем точность
    acc = accuracy_score(y_test, preds)

    mlflow.set_tracking_uri("http://localhost:5000")

    # Логируем параметры и метрики
    mlflow.log_param("C", C_param)
    mlflow.log_metric("accuracy", acc)

    # Логируем модель
    mlflow.sklearn.log_model(model, "model")

    print(f"Accuracy: {acc:.4f}")
