import controller

from telebot import TeleBot, types
#import os
 
TOKEN = '5615159193:AAFAm4a5YKA3w2EhtlvwS9qkDEzL0jqalUo'
 
bot = TeleBot(TOKEN)

dct = {}
@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    dct[msg.from_user.id] = []
    bot.send_message(chat_id=msg.from_user.id, text=f'Здравствуйте. Вы открыли телефонный справочник!')
    #menu()

# def greeting():
#     print()
#     print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')

''''
def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # Работает
        print('3. Скопировать данные в файл?')  # надо добавить копирование в json
        print('4. Сохранить в нашу базу данных?') # надо сделать
        print('5. Поиск записи')  # работает
        print('6. Выход\n')   # работает
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
        if number =='6':
            break
 '''

#greeting()
#menu()

bot.polling()