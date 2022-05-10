FROM python:3.8
WORKDIR /home
ENV TELEGRAM_API_TOKEN="5332728733:AAF_sCBOwdTpOdXhomKPuMszQSuJx4PHw20"
RUN pip install -U pip aiogram && apt-get update && pip install requests && pip install beautifulsoup4
COPY *.py ./
ENTRYPOINT ["python3", "main.py"]