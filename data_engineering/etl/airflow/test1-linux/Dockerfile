FROM apache/airflow:2.9.3-python3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    which airflow && airflow version