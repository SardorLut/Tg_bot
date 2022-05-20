FROM python:3.8
WORKDIR /home
ARG TELEGRAM_API_TOKEN=your_token
ENV TELEGRAM_API_TOKEN="${TELEGRAM_API_TOKEN}"
RUN pip install -U pip aiogram && apt-get update && pip install requests && pip install beautifulsoup4
COPY *.py ./
ENTRYPOINT ["python3", "main.py"]