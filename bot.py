import telebot
from telebot import types
bot = telebot.TeleBot('5669276782:AAEJH2fX07yB9ycqeCLWJdp8RpusIwtyNUg')
@bot.message_handler(commands = [ 'start' ])
def start(message):
    name = (str(message.from_user.first_name))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    help = types.KeyboardButton('🤷‍♂️HELP🤷‍♂️')
    markup.add(help)
    bot.send_message(message.chat.id,'Salut! '+name+'\n Sunt OOGWAY bot si reprezint compania RoboCode 👨‍💻\n (click help)',reply_markup=markup)
    sti = open('img/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)


@bot.message_handler()
def help_s(message):
    if message.text =='🤷‍♂️HELP🤷‍♂️':
        print("gg")
        help(message)


@bot.message_handler(commands=['help'])
def help(message):

    markup = types.InlineKeyboardMarkup(row_width= 2)
    web = types.InlineKeyboardButton("WebSite 🤖", url = 'https://robocode.md/')
    test = types.InlineKeyboardButton("Locații 📍", callback_data="gps")
    cnts = types.InlineKeyboardButton("Contacte ☎️", callback_data="cont")
    markup.add(web,test,cnts)
    bot.send_message(message.chat.id, "<b>Uite câteva comenzi :     </b>",reply_markup=markup,parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def gps(call: types.CallbackQuery):
    cid = call.message.chat.id
    if call.data == "gps":
        markup = types.InlineKeyboardMarkup(row_width= 1)
        cio = types.InlineKeyboardButton("•Ciocana•", url = 'https://g.page/robocode-ciocana?share')
        bota = types.InlineKeyboardButton("•Botanica•", url = 'https://g.page/Robocode-botanica?share')
        bui = types.InlineKeyboardButton("•Buiucani•", url = 'https://g.page/robocode-buiucani?share')
        cent = types.InlineKeyboardButton("•Râșcani•", url = 'https://goo.gl/maps/h6kmaN2dBLC9Rvw36')
        bal = types.InlineKeyboardButton("•Bălți•", url = 'https://goo.gl/maps/6DjTdpyFddcPuV3t6')

        markup.add(cio,bota,bui,cent,bal)
        bot.send_message(cid,'<b>Alege una dintre locații👨‍💻📍</b>',reply_markup=markup,parse_mode='html')
    elif call.data == "cont":
        markup = types.InlineKeyboardMarkup(row_width= 1)
        tele = types.InlineKeyboardButton("Telefon",callback_data="tel")
        gmail = types.InlineKeyboardButton("Gmail", url = 'mailto:info@robocode.pro')
        you = types.InlineKeyboardButton("YouTube", url = 'https://www.youtube.com/channel/UCAw8QP5JiYbLBrQRdKXhAIg')
        ig = types.InlineKeyboardButton("Instagram", url = 'https://www.instagram.com/robocode.md/')
        fb = types.InlineKeyboardButton("FaceBook", url = 'https://www.facebook.com/Robocode.md/')

        markup.add(tele,gmail,you,ig,fb)
        bot.send_message(cid,'<b>Contacte ☎️</b>',reply_markup=markup,parse_mode='html')
    if call.data == "tel":
        bot.send_message(cid,'<b>+373 22 011 188</b>',parse_mode='html',)







bot.infinity_polling()