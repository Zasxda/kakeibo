FROM python:3.11-slim

WORKDIR /workspace/kakeibo

RUN pip install --no-cache-dir uv

COPY pyproject.toml ./
COPY uv.lock ./

RUN uv sync --frozen --no-install-project

COPY . .

CMD ["uv", "run", "python", "manage.py", "runserver","0.0.0.0:8000"]
