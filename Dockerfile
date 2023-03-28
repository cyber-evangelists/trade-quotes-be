FROM python:3.10.0

WORKDIR /app

RUN pip install poetry

RUN python -m poetry config virtualenvs.in-project true

COPY pyproject.toml .

RUN python -m poetry install

COPY . .

CMD python -m poetry run uvicorn lib.main:app --host 0.0.0.0
