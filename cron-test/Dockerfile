FROM python:3.12-slim

WORKDIR /app

COPY write_hej.py .

RUN useradd --uid 1000 --create-home appuser

USER appuser

CMD ["python", "/app/write_hej.py"]