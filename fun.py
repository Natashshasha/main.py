# ======================================= Развлечения
import requests
import bs4  # BeautifulSoup4
from telebot import types
from io import BytesIO
import json

# -----------------------------------------------------------------------
def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Собачки":
        bot.send_photo(chat_id, photo=get_dogURL(), caption="Вот тебе собачка!")

    elif ms_text == "Лисята":
        bot.send_photo(chat_id, photo=get_foxURL(), caption="Вот тебе лисёнок!")

    if ms_text == "Котики":
        bot.send_photo(chat_id, photo=get_catURL(), caption="Вот тебе котенок!")

    elif ms_text == "Странные анекдоты":
        bot.send_message(chat_id, text=get_anekdot())

    elif ms_text == "Прислать фильм":
        send_film(bot, chat_id)

    elif ms_text == "Угадай кто?":
        get_ManOrNot(bot, chat_id)

    elif ms_text == "Цитаты":
        bot.send_message(chat_id, text=getRandomquot())

    elif ms_text == "Факт":
        bot.send_message(chat_id, text=get_fact())

    elif ms_text == "Курс биткоина":
        bot.send_message(chat_id, text=get_bitcoin())



# -----------------------------------------------------------------------
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('.anekdot_text')
        for result in result_find:
            array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""

# -----------------------------------------------------------------------
def get_foxURL():
    contents = requests.get('https://randomfox.ca/floof/').json()
    return contents['image']
# -----------------------------------------------------------------------
def get_dogURL():
    contents = requests.get('https://random.dog/woof.json').json()
    return contents['url']
# -----------------------------------------------------------------------
def get_catURL():
    contents = requests.get('http://aws.random.cat//meow').json()
    return contents['file']
# -----------------------------------------------------------------------
def get_randomFilm():
    url = 'https://randomfilm.ru/'
    infoFilm = {}
    req_film = requests.get(url)
    soup = bs4.BeautifulSoup(req_film.text, "html.parser")
    result_find = soup.find('div', align="center", style="width: 100%")
    infoFilm["Наименование"] = result_find.find("h2").getText()
    names = infoFilm["Наименование"].split(" / ")
    infoFilm["Наименование_rus"] = names[0].strip()
    if len(names) > 1:
        infoFilm["Наименование_eng"] = names[1].strip()

    images = []
    for img in result_find.findAll('img'):
        images.append(url + img.get('src'))
    infoFilm["Обложка_url"] = images[0]

    details = result_find.findAll('td')
    infoFilm["Год"] = details[0].contents[1].strip()
    infoFilm["Страна"] = details[1].contents[1].strip()
    infoFilm["Жанр"] = details[2].contents[1].strip()
    infoFilm["Продолжительность"] = details[3].contents[1].strip()
    infoFilm["Режиссёр"] = details[4].contents[1].strip()
    infoFilm["Актёры"] = details[5].contents[1].strip()
    infoFilm["Трейлер_url"] = url + details[6].contents[0]["href"]
    infoFilm["фильм_url"] = url + details[7].contents[0]["href"]

    return infoFilm
#----------------------------------------------------------------------------
def getRandomquot():
    array_anekdots = []
    req_anek = requests.get('https://randstuff.ru/saying/')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('table', class_='text')
        for result in result_find:
            array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""

#-----------------------------------------------------------------------
def get_fact():
    array_anekdots = []
    req_anek = requests.get('https://randstuff.ru/fact/random')
    if req_anek.status_code == 200:
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('table', class_='text')
        for result in result_find:
            array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0:
        return array_anekdots[0]
    else:
        return ""
#-----------------------------------------------------------------------
def get_ManOrNot(bot, chat_id):

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Проверить", url="https://vc.ru/dev/58543-thispersondoesnotexist-sayt-generator-realistichnyh-lic")
    markup.add(btn1)

    req = requests.get("https://thispersondoesnotexist.com/image", allow_redirects=True)
    if req.status_code == 200:
        img = BytesIO(req.content)
        bot.send_photo(chat_id, photo=img, reply_markup=markup, caption="Этот человек реален?")
# -----------------------------------------------------------------------
def send_film(bot, chat_id):
    film = get_randomFilm()
    info_str = f"<b>{film['Наименование']}</b>\n" \
               f"Год: {film['Год']}\n" \
               f"Страна: {film['Страна']}\n" \
               f"Жанр: {film['Жанр']}\n" \
               f"Продолжительность: {film['Продолжительность']}"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Трейлер", url=film["Трейлер_url"])
    btn2 = types.InlineKeyboardButton(text="СМОТРЕТЬ онлайн", url=film["фильм_url"])
    markup.add(btn1, btn2)
    bot.send_photo(chat_id, photo=film['Обложка_url'], caption=info_str, parse_mode='HTML', reply_markup=markup)
#------------------------------------------------------------------------
def get_bitcoin():
    contents = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    date = contents['time']['updateduk']
    cost = contents['bpi']['EUR']['rate']
    return 'Сегодня, ' + date + ' по Британскому времени' + '\n' + 'курс биткоина: ' + cost + ' евро'