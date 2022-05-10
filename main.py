import os
import string
from get_list import get_list
from aiogram import Bot, types, Dispatcher, executor
from Globals import Globals
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if Globals.language == 'rus':
        await message.answer('Данный бот показывает курс ЦБ РФ\n'
                             '/russian переключить язык на русский\n'
                             '/english переключить язык на английский\n'
                             '/list вывести список валюты, буквенный код и в скобках единицы валюты и название\n'
                             'Для вывода текущего курса нужно ввести буквенный код')
    else:
        await message.answer('This bot shows the exchange rate of the Central Bank of the Russian Federation\n'
                             '/russian switch language to russian\n'
                             '/english switch language to english\n'
                             '/list display a list of currencies, character code, unit and currency name in brackets\n'
                             'To display the current rate, you need to enter a character code')


@dp.message_handler(commands=['russian'])
async def switch_to_rus(message: types.Message):
    Globals.url = 'https://www.cbr.ru/currency_base/daily/'
    Globals.language = 'rus'
    await message.answer('Вы переключились на русский язык, '
                         'введите /help чтобы узнать информацию о боте')


@dp.message_handler(commands=['english'])
async def switch_to_eng(message: types.Message):
    Globals.url = 'https://www.cbr.ru/eng/currency_base/daily/'
    Globals.language = 'eng'
    await message.answer('You have switched to Russian, '
                         'enter /help to find out information about the bot')




@dp.message_handler(commands=['list'])
async def get_list_currency(message: types.Message):
    try:
        all_1 = get_list()
        n = ""
        for i in range(len(all_1)):
            s = [s for s in all_1[i] if s in string.ascii_uppercase]
            if len(all_1[i]) == 3 and len(s) and all_1[i] != "SDR":
                char = all_1[i]
                unit = all_1[i + 1]
                name = all_1[i + 2]
                n += f"{char} ({unit} {name})\n"
        await message.answer(n)
    except AttributeError:
        await message.answer("Попробуйте позднее сайт, не отвечает" if Globals.language == "rus"
                             else "Try later site not responding")

@dp.message_handler()
async def get_currency(message: types.Message):
    try:
        all_1 = get_list()
        for i in range(len(all_1)):
            s = [s for s in all_1[i] if s in string.ascii_uppercase]
            if len(all_1[i]) == 3 and len(s) and message.text == all_1[i] and all_1[i] != "SDR":
                cost = all_1[i + 3]
                unit = all_1[i + 1]
                name = all_1[i + 2]
                r = "рублей" if Globals.language == "rus" else "rubles"
                await message.answer(f"{unit} {name} = {cost} {r}")
    except AttributeError:
        await message.answer("Попробуйте позднее сайт, не отвечает" if Globals.language == "rus"
                             else "Try later site not responding")

executor.start_polling(dp, skip_updates=True)
