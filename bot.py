import telebot
from telebot import types

bot = telebot.TeleBot("7482111857:AAH1CYaBKe50hHj4Q2pRmMGQQzgW0Cnr__g")


@bot.message_handler(commands=['quiz'])
def question(massage):
    markup = types.InlineKeyboardMarkup(row_width=2)

    iron = types.InlineKeyboardButton("nima gap", callback_data="answer_iron")
    cotton = types.InlineKeyboardButton("tinch", callback_data="answer_cotton")
    same = types.InlineKeyboardButton("ha yaxshi", callback_data="answer_same")
    no_answer = types.InlineKeyboardButton("nima", callback_data="no_answer")

    markup.add(iron, cotton, same, no_answer)

    bot.send_message(massage.chat.id, "Вопрос", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(callback):
    if callback.message:
        bot.send_message(callback.message.chat.id, "Ваш: ")

bot.polling()
