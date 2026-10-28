# Headless Chromium for the Selenium lecture steps. Runs without a desktop.
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    CHROME_BIN=/usr/bin/chromium \
    RESULTS_DIR=/results

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
COPY tests ./tests
RUN python -m pip install --upgrade pip \
    && python -m pip install ".[dev]"

VOLUME ["/results"]
CMD ["python", "-m", "fill_out_form", "--headless", "--screenshots", "/results"]
