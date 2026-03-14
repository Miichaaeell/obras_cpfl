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
    tzdata \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app

# cria cron job
RUN echo "*/2 * * * * cd /app && PYTHONPATH=/app/src poetry run python -m obras_cpfl.main >> /proc/1/fd/1 2>> /proc/1/fd/2" > /etc/cron.d/obras-cpfl

RUN chmod 0644 /etc/cron.d/obras-cpfl && crontab /etc/cron.d/obras-cpfl

CMD ["cron", "-f"]
