FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.3.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    gcc \
    cron \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root

COPY . /app

RUN echo "0 8 * * * cd /app && PYTHONPATH=/app/src /usr/local/bin/python -m obras_cpfl.main >> /proc/1/fd/1 2>> /proc/1/fd/2" > /etc/cron.d/obras-cpfl

RUN chmod 0644 /etc/cron.d/obras-cpfl && crontab /etc/cron.d/obras-cpfl

CMD ["cron", "-f"]
