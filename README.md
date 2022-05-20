<h2 style="font-style:italic"><span style="font-size:22px"><strong>Бот для телеграма</strong></span></h2>

<hr />
<p><span style="font-size:16px">Телеграм бот, который отслеживает текущий курс валют по отношению к рублю от ЦБ РФ</span></p>

<h2 style="font-style:italic"><strong>Установка</strong></h2>

<table border="1" cellpadding="1" cellspacing="1" dir="ltr" style="width:500px">

    git clone https://github.com/SardorLut/Tg_bot.git
    cd Tg_bot
    sudo docker build -t tg --build-arg TELEGRAM_API_TOKEN=<token> ./
    sudo docker run -d --name tgbot tg
</table>