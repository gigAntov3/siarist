FROM python:3.11.9-slim

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

WORKDIR /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]