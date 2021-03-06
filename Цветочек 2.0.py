# Вариант 1 - самый простой чат бот, просто отзывается
import bs4
import telebot  # pyTelegramBotAPI	4.3.1
import math
import requests
from telebot import types
import requests


# три глобальные переменные
response_to_input = ""  # для формирования проверки введенного имени/возраста/ответа на задачу
userName = ""  # для запоминания имени пользователя
userAge = -1  # для запоминания возраста
bot = telebot.TeleBot('5168714419:AAFRFYftvFE1DTDCMzG-b0dQ8OSSg43O2uI')  # Создаем экземпляр бота @Ivanov_Ivan_1MD19_bot

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Главное меню")
    button2 = types.KeyboardButton("Помощь")
    markup.add(button1, button2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user))
def get_dogURL():
    url = ""
    req = requests.get('https://random.dog/woof.json')
    if req.status_code == 200:
        r_json = req.json()
        url = r_json['url']
        # url.split("/")[-1]
    return url

def get_foxURL():
    url = ""
    req = requests.get('https://randomfox.ca/floof/')
    if req.status_code == 200:
        r_json = req.json()
        url = r_json['image']
        # url.split("/")[-1]
    return url

def get_quote():
    array_anekdots = []
    req_anek = requests.get('https://www.plerdy.com/ru/blog/top-215-motivational-quotes/')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('.entry-content')
        for result in result_find:
            print(result)

            # array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""


def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]

def get_news():
    array_anekdots = []
    req_anek = requests.get('https://www.banki.ru/news/lenta')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('.doFpcq')
        for result in result_find:
            print(result)

            # array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""



# -----------------------------------------------------------------------

# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    # две заготовки кнопок на будущее
    aback = types.KeyboardButton("К Анкете")
    back = types.KeyboardButton("Главное меню")
    # ниже обявляем что будем использвать значения из глобальных переменных, объявленных выше
    global response_to_input
    global userAge
    global userName
    ms_text = message.text

    if ms_text == "Меню" or ms_text == "Главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Развлечения"),
                   types.KeyboardButton("WEB-камера"),
                   types.KeyboardButton("Управление"),
                   types.KeyboardButton("Анкета"),
                   types.KeyboardButton("Об Авторе"))
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Прислать собаку"),
                   types.KeyboardButton("Прислать лису"),
                   types.KeyboardButton("Прислать мотивирующую цитату"),
                   types.KeyboardButton("Прислать анекдот"),
                   types.KeyboardButton("Игры"),
                   back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "Игры":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Игра Камень-ножницы-бумага"),
                   types.KeyboardButton("Игра в 21"),
                   back)
        bot.send_message(chat_id, text="Игры", reply_markup=markup)

    elif ms_text == "Анкета" or ms_text == "Дз" or ms_text == "ДЗ" or ms_text == "К Анкете":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # далее у меня добавляются кнопки, в зависимости от введенного имени и/или возраста
        if not userName == "" and not userAge == -1:
            bot.send_message(chat_id, text="Твой позывной " + userName + ", тебе " + str(userAge) + " лет")
            markup.add(types.KeyboardButton("Выведи имя x5"),
                       types.KeyboardButton("О возрасте"),
                       types.KeyboardButton("Переверни имя"),
                       types.KeyboardButton("Длина имени"),
                       types.KeyboardButton("Имя с большой буквы")
                       )
        elif not userName == "":
            bot.send_message(chat_id, text="Твой позывной " + userName)
            markup.add(types.KeyboardButton("Выведи имя x5"),
                       types.KeyboardButton("Переверни имя"),
                       types.KeyboardButton("Имя с большой буквы"))
        elif not userAge == -1:
            bot.send_message(chat_id, text="Твой возраст " + str(userAge))
            markup.add(types.KeyboardButton("О возрасте"))
        if not userName == "" or not userAge == -1:
            markup.add(types.KeyboardButton("Сбросить имя и возраст"))
        # кнопки ниже есть всегда
        markup.add(types.KeyboardButton("Ввод имени"),
                   types.KeyboardButton("Ввод возроста"),
                   types.KeyboardButton("Задача"),
                   back)

        bot.send_message(chat_id, text="Выбери что надо", reply_markup=markup)

    elif ms_text == "Ввод имени" or ms_text == "Ввести имя заново":
        bot.send_message(chat_id, text="Введи свое имя")

        response_to_input = ms_text + " ответ"  # формирование строки для перехода в elif ниже
        # response_to_input=Ввод имени ответ, тк ms_text=Ввод имени

    # функция проверки правльно введенного имени
    elif response_to_input == "Ввод имени ответ" or response_to_input == "Ввести имя заново ответ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if " " in ms_text:
            markup.add(types.KeyboardButton("Ввести имя заново"),
                       aback, back)
            bot.send_message(chat_id, text="Ошибка в имени", reply_markup=markup)
        else:
            # если все хорошо то запоминаем имя
            userName = ms_text
            markup.add(aback, back)
            bot.send_message(chat_id, text="Ваше имя: " + userName, reply_markup=markup)
        response_to_input = ""

    elif ms_text == "Ввод возроста" or ms_text == "Ввести возраст заново":
        bot.send_message(chat_id, text="Введи свой возраст")
        response_to_input = ms_text + " ответ"

    elif response_to_input == "Ввод возроста ответ" or response_to_input == "Ввести возраст заново ответ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        try:
            if int(ms_text) < 0 or int(ms_text) > 150:
                markup.add(types.KeyboardButton("Ввести возраст заново"),
                           aback, back)
                bot.send_message(chat_id, text="Ошибка в возрасте", reply_markup=markup)
            else:
                userAge = ms_text
                markup.add(aback, back)
                bot.send_message(chat_id, text="Ваш возраст: " + userAge, reply_markup=markup)
        except:
            markup.add(types.KeyboardButton("Ввести возраст заново"),
                       aback, back)
            bot.send_message(chat_id, text="Ошибка в возрасте", reply_markup=markup)
        response_to_input = ""

    elif ms_text == "Сбросить имя и возраст":
        userAge = -1
        userName = ""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        bot.send_message(chat_id, text="Параметры сброшены", reply_markup=markup)

    elif ms_text == "Выведи имя x5" and not userName == "":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        bot.send_message(chat_id, text=userName * 5, reply_markup=markup)

    elif ms_text == "О возрасте" and not int(userAge) == -1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        if int(userAge) > 20:
            bot.send_message(chat_id, text="Тебе больше 20", reply_markup=markup)
        if int(userAge) < 20:
            bot.send_message(chat_id, text="Тебе меньше 20", reply_markup=markup)
        if int(userAge) == 20:
            bot.send_message(chat_id, text="Тебе 20 лет", reply_markup=markup)

    elif ms_text == "Переверни имя" and not userName == "":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        if len(userName) >= 5:
            bot.send_message(chat_id,
                             text=userName[::-1] + "\n" + userName[1:-1] + "\n" + userName[-3:] + "\n" + userName[:5],
                             reply_markup=markup)
        else:
            bot.send_message(chat_id, text=userName[::-1] + "\n" + userName[1:-1] + "\n" + userName[-3:],
                             reply_markup=markup)

    elif ms_text == "Длина имени" and not int(userAge) == -1 and not userName == "":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        bot.send_message(chat_id, text="Длина твоего имени " + str(len(userName)))
        i = 0
        summ = 0
        mult = 1
        while i < len(userAge):
            summ = summ + int(userAge[i])
            mult = mult * int(userAge[i])
            i += 1
        bot.send_message(chat_id,
                         text="Сумма твоего возраста " + str(summ) + "\nПроизведение твоего возраста " + str(mult),
                         reply_markup=markup)

    elif ms_text == "Имя с большой буквы" and not userName == "":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        bot.send_message(chat_id, text=userName.upper() + " " + userName.lower() + " " + userName[
                                                                                         ::-1].capitalize() + " " + userName.capitalize(),
                         reply_markup=markup)

    elif ms_text == "Задача" or ms_text == "Задачу заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        bot.send_message(chat_id, "Сколько будет 2+2*2?")
        response_to_input = ms_text + " ответ"

    elif response_to_input == "Задача ответ" or response_to_input == "Задачу заново ответ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(aback, back)
        if int(ms_text) == 6:
            bot.send_message(chat_id, text="Правильно", reply_markup=markup)
        else:
            markup.add(types.KeyboardButton("Задачу заново"))
            bot.send_message(chat_id, text="Неправильно", reply_markup=markup)
        response_to_input = ""

    elif ms_text == "/dog" or ms_text == "Прислать собаку":  # .........................................................
        bot.send_photo(chat_id, photo=get_dogURL(), caption="Вот тебе собачка!")

    elif ms_text == "Прислать лису":
        bot.send_photo(chat_id, photo=get_foxURL(), caption="Вот тебе лиса!")

    elif ms_text == "Прислать мотивирующую цитату":
        bot.send_photo(chat_id, text=get_quote(), caption="Вот тебе цитата!")

    elif ms_text == "Прислать анекдот":  # .............................................................................
        bot.send_message(chat_id, text=get_anekdot())

    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text in gameRPS.values:
        gameRSP = getGame(chat_id)
        if gameRSP is None:  # если мы случайно попали в это меню, а объекта с игрой нет
            goto_menu(bot, chat_id, "Выход")
            return
        text_game = gameRSP.playerChoice(ms_text)
        bot.send_message(chat_id, text=text_game)
        gameRSP.newGame()

    elif ms_text == "Игра в 21":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Игра Камень-ножницы-бумага ":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Киселева Наталья")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="")
        key1.add(btn1)
        img = open('resources/ak.jpg', "r+b")
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()
