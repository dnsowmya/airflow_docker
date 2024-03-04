FROM apache/airflow:2.0.1
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
FROM --platform=linux/amd64 amazonlinux:2018.03
COPY requirements.txt /requirements.txt
