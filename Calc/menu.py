import os
from telebot import TeleBot
import main as m
import datetime
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
    elif text == '+++':
        bot.register_next_step_handler(message, sum_complex_numbers)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '- - -':
        bot.register_next_step_handler(message, subtraction_complex_numbers)
        bot.reply_to(message, m.MESSAGE_1)
    else:
        bot.reply_to(message, text='Вы прислали: ' + text +
                        ', а должны были арифметическое действие')
    
    dtn = datetime.datetime.now()
    botlogfile = open('log_calculator.txt', 'a', encoding='utf-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + 
            message.from_user.first_name, message.from_user.id, 
            'операция: ' + text, file=botlogfile)
    botlogfile.close()


def sum(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2) 


def sum_complex_numbers(msg):
    c = list(msg.text.split())
    x = c[0]
    y = c[1]
    if x[-1] == 'j':
        num = 0
        ncom2 = int(x[:-1])
    if y[-1] == 'j':
        numm = 0 
        ncom4 = int(y[:-1])
    
    if x[0]=='-':
        z = -1
    else:
        z = 1
    if y[0]=='-':
        zz = -1
    else:
        zz = 1
    if x[0] == '-' or x[0]=='+':
        x = x[1:]

    if y[0] == '-' or y[0]=='+':
        y = y[1:]  
        
        
    if '+' in x:
        ncom1 = x.rpartition('+')[0] 
        ncom1 = ncom1[:-1]
        
        ncom2 = int(ncom1)*z
        
        cc = x.rpartition('+')[1] 
        num = int(x.rpartition('+')[2])
        if cc == '-':
            num = (-1)*num
    elif '-' in x:
        ncom1 = x.rpartition('-')[0] 
        ncom1 = ncom1[:-1]
        
        ncom2 = int(ncom1)*z
        
        cc = x.rpartition('-')[1] 
        num = int(x.rpartition('-')[2])*(-1) 
        
        
    if '+' in y:
        ncom3 = y.rpartition('+')[0]
        ncom3 = ncom3[:-1]
        ncom4 = int(ncom3)*zz
        ccc = y.rpartition('+')[1] 
        numm = int(y.rpartition('+')[2])

    elif '-' in y:
        ncom3 = y.rpartition('-')[0]
        ncom3 = ncom3[:-1]
        ncom4 = int(ncom3)*zz
        ccc = y.rpartition('-')[1] 
        numm = int(y.rpartition('-')[2])*(-1) 
        
    jsum = ncom2+ncom4
    sum1 = num + numm
    if sum1<0:
        res = f'{jsum}j{sum1}'
    else:
        res = f'{jsum}j+{sum1}'
        
    

    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {res}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2) 



def subtraction(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    

def subtraction_complex_numbers(msg):
    c = list(msg.text.split())
    x = c[0]
    y = c[1]
    if x[-1] == 'j':
        num = 0
        ncom2 = int(x[:-1])
    if y[-1] == 'j':
        numm = 0 
        ncom4 = int(y[:-1])
    
    if x[0]=='-':
        z = -1
    else:
        z = 1
    if y[0]=='-':
        zz = -1
    else:
        zz = 1
    if x[0] == '-' or x[0]=='+':
        x = x[1:]

    if y[0] == '-' or y[0]=='+':
        y = y[1:]  
        
        
    if '+' in x:
        ncom1 = x.rpartition('+')[0] 
        ncom1 = ncom1[:-1]
        
        ncom2 = int(ncom1)*z
        
        cc = x.rpartition('+')[1] 
        num = int(x.rpartition('+')[2])
        if cc == '-':
            num = (-1)*num
    elif '-' in x:
        ncom1 = x.rpartition('-')[0] 
        ncom1 = ncom1[:-1]
        
        ncom2 = int(ncom1)*z
        
        cc = x.rpartition('-')[1] 
        num = int(x.rpartition('-')[2])*(-1) 
        
        
    if '+' in y:
        ncom3 = y.rpartition('+')[0]
        ncom3 = ncom3[:-1]
        ncom4 = int(ncom3)*zz
        ccc = y.rpartition('+')[1] 
        numm = int(y.rpartition('+')[2])

    elif '-' in y:
        ncom3 = y.rpartition('-')[0]
        ncom3 = ncom3[:-1]
        ncom4 = int(ncom3)*zz
        ccc = y.rpartition('-')[1] 
        numm = int(y.rpartition('-')[2])*(-1) 
        
    jsum = ncom2 - ncom4
    sum1 = num - numm
    if sum1<0:
        res = f'{jsum}j{sum1}'
    else:
        res = f'{jsum}j+{sum1}'
        
    

    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {res}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)  

    
def devision(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    
    
def mult(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


bot.polling()