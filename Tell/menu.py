import controller
import operations
import export_data
import searchcontact
import import_data

from telebot import TeleBot, types
#import os
 
TOKEN = '5615159193:AAFAm4a5YKA3w2EhtlvwS9qkDEzL0jqalUo'
 
bot = TeleBot(TOKEN)

dct = {}
@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    dct[msg.from_user.id] = []
    bot.send_message(chat_id=msg.from_user.id, text=f'Здравствуйте. Вы открыли телефонный справочник!')
    bot.send_message(chat_id=msg.from_user.id, text=f'1. Добавить новую запись \n 2. Вывод записей на экран \n 3. Скопировать данные в файл?\n 4. Сохранить в нашу базу данных?\n 5. Поиск записи')
    n = msg.text
    
    if n == '1':
        temp = operations.new_contact()
    #enter = input('Нажмите Enter для завершения')
'''
    elif n == '2':
        print(
            'Выберите формат отображения данных: 1 - Построчно; 2 - В одну строку', sep='\n')
        num = int(input())
        if num == 1 or num == 2:
            operations.read_contact(num)
        enter = input('Нажмите Enter для выхода в меню ')

    elif n == '3':
        '''
        # если вы все данные из своего файла скопируете в файл, 
        # который укажет пользователь, то это можно считать экспортом
'''
        file_name_expott = input(
            'Нипишите имя файла куда вы хотите скопировать данные: ')
        print('Выберите формат экспорта данных:',
              '1 - xml', '2 - json', sep='\n')
        num_exp = input()
        if num_exp == '1':
            export_data.export_to_xml(file_name_expott)
            print('Данные успешно экспортированы в формате xml!\n')
        elif num_exp == '2':
            export_data.csv_to_json(file_name_expott)
            print(f'Данные успешно сохранены в файл {file_name_expott}.json\n')
        else:
            print('Пожалуста, введите номер пункта меню: ')
            enter = input('Нажмите Enter для выхода в меню ')
        enter = input('Нажмите Enter для завершения')

    elif n == '4':
        '''
        # считывание и сохранение, в вашу базу, записей из файла, 
        # который указал пользователь
'''
        num = int(input(
            'Выберете тип файла, из которого будете брать данные 1 - csv, 2 - json'))
        if num == 1:
            arr1 = import_data.copy_cont()
            import_data.write_csv(arr1)
        if num == 2:
            import_data.copy_cont_json()
        enter = input('Нажмите Enter для завершения')

    elif n == '5':
        user_search = input('Введите имя для поиска?: ')
        searchcontact.searchcontact(user_search)
        enter = input('Нажмите Enter для завершения')     
 '''

#greeting()
#menu()

bot.polling()