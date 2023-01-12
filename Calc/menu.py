import os
from telebot import TeleBot, types
import main as m
import translation
import datetime
import codecs
os.chdir(os.path.dirname(__file__))

token = ''
bot = TeleBot(token)

@bot.message_handler(commands=m.USER_COMMANDS)
def send_welcome(message):
    cmd = message.text.lstrip('/')
    if cmd == 'start':
        bot.reply_to(message, m.OPERATIONS)
    else:
        bot.reply_to(message, m.INFO_MESSAGE)


@bot.message_handler()
def send_welcome(message):
    
    text = message.text
    if text == '+':
        bot.register_next_step_handler(message, sum)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '-':
        bot.register_next_step_handler(message, subtraction)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '//' or text == '/':
        bot.register_next_step_handler(message, devision)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '*':
        bot.register_next_step_handler(message, mult)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == 'log':
        bot.register_next_step_handler(message, logir_print)
        bot.reply_to(message, m.MESSAGE_3)

    else:
        bot.reply_to(message, text='Вы прислали: ' + text +
                        ', а должны были арифметическое действие')
    logir(message)

def logir(message):
    dtn = datetime.datetime.now()
    
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(
            f'\n Chat {message.chat.id} User: {message.from_user.first_name} Data: {dtn} Message 1: {message.text}')


def logir_print(msg):
        
    bot.send_document(chat_id=msg.from_user.id, document=open(f'log', 'rb'))
             

def chek(num):
    if 'j' in num:
        num = translation.transl(num)
    elif num.isdigit():
        num = int(num)
    elif '.' in num:
        num = float(num)
    elif ',' in num:
        num = num.replace(',', '.')  
        num = float(num)
    return num
    

def sum(msg):
    k = msg.text.split()
    a = chek(k[0])
    b = chek(k[1])
    
    answer = a + b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {answer}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(f'Message 2 {msg.text} , Answer {answer}')


def subtraction(msg):
    k = msg.text.split()
    a = chek(k[0])
    b = chek(k[1])
    answer = a - b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {answer}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(f'Message 2 {msg.text} , Answer {answer}')
    
    
def devision(msg):
    k = msg.text.split()
    a = chek(k[0])
    b = chek(k[1])
    if b == 0:
        bot.send_message(chat_id=msg.from_user.id, text=f'На 0 делить нельзя!')
        exit()
    answer = a / b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {answer}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(f'Message 2 {msg.text} , Answer {answer}')
    
    
def mult(msg):
    k = msg.text.split()
    a = chek(k[0])
    b = chek(k[1])
    answer = a * b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {answer}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(f'Message 2 {msg.text} , Answer {answer}')


bot.polling()