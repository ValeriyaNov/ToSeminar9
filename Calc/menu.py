import os
from telebot import TeleBot, types
import main as m
import datetime
import codecs
os.chdir(os.path.dirname(__file__))

token = '5615159193:AAFAm4a5YKA3w2EhtlvwS9qkDEzL0jqalUo'
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

    elif text == '***':
        bot.register_next_step_handler(message, mult_complex_numbers)
        bot.reply_to(message, m.MESSAGE_1)
    elif text == '///':
        bot.register_next_step_handler(message, dev_complex_numbers)
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
            f'\n Chat {message.chat.id} User: {message.from_user.first_name} Data: {dtn} Message: {message.text} Answer: {message.text}')



def logir_print(msg):
        
    bot.send_document(chat_id=msg.from_user.id, document=open(f'log', 'rb'))
             


def sum(msg):
    a, b = map(float, msg.text.split())
    answer = a + b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {answer}')
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
        
    answer = res

    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {answer}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2) 



def subtraction(msg):
    a, b = map(float, msg.text.split())
    answer = a - b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {answer}')
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
    answer = res
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {answer}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)  

    
def devision(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    
    
def mult(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


def mult_complex_numbers(msg):
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
            
    mult = num*numm - ncom2*ncom4
    jmult = num*ncom4 + numm*ncom2
    if mult<0:
        res = f'{jmult}j{mult}'
    else:
        res = f'{jmult}j+{mult}'
            
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {res}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)
    

def dev_complex_numbers(msg):
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
            
    dev = (num*numm + ncom2*ncom4)/(numm**2 + ncom4**2)
    jdev = (ncom2*numm - num*ncom4)/(numm**2 + ncom4**2)
    num*ncom4 + numm*ncom2
    if dev<0:
        res = f'{jdev}j{dev}'
    else:
        res = f'{jdev}j+{dev}'
        
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {res}')
    bot.send_message(chat_id=msg.from_user.id, text=m.MESSAGE_2)


bot.polling()