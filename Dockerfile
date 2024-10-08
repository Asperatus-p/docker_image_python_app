FROM python:3.9

RUN pip install --upgrade pip

COPY app.py /app.py

CMD ["python", "/app.py"]
