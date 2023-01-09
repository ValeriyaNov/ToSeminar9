import csv
import export_data
import import_data
from telebot import TeleBot, types
TOKEN = '5615159193:AAFAm4a5YKA3w2EhtlvwS9qkDEzL0jqalUo'
 
bot = TeleBot(TOKEN)
import os
os.chdir(os.path.dirname(__file__))


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'Здравствуйте. Вы открыли телефонный справочник!')
    bot.send_message(chat_id=msg.from_user.id, text=f'1. Добавить новую запись \n 2. Вывод записей на экран \n 3. Скопировать данные в файл?\n 4. Сохранить в нашу базу данных?\n 5. Поиск записи\n 6. Сохранить в нашу базу данных все контакты')

@bot.message_handler()
def answer(msg: types.Message):
    
    n = msg.text
    
    if n == '1':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите имя, фамилию, номер и описание через пробел!')
        print('Данные сохранены')

    if n == '2':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text=f'Выберете формат: 1 - Построчно; 2 - В одну строку')

    if n == '3':
        bot.register_next_step_handler(msg, answer3)
        bot.send_message(chat_id=msg.from_user.id, text=f'Напишите имя файла, через пробел напишите номер формата экспорта данных: 1 - xml, 2 - json')
    
    if n == '4':
        bot.register_next_step_handler(msg, answer4)
        bot.send_message(chat_id=msg.from_user.id, text=f'Выберете тип файла, из которого будете брать данные 1 - csv, 2 - json и через пробел введите имя файла и через пробел имя человека и пришлите файл')

    if n == '5':
        bot.register_next_step_handler(msg, answer5)
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите имя для поиска') 
    if n == '6':
        bot.register_next_step_handler(msg, answer11)
        bot.send_message(chat_id=msg.from_user.id, text=f'Пришлите файл, с которого необходимо скопировать данные')
        #bot.register_next_step_handler(msg, answer6)
        #bot.send_message(chat_id=msg.from_user.id, text=f'Выберете тип файла, из которого будете брать данные 1 - csv, 2 - json и через пробел введите имя файла')



@bot.message_handler()
def answer1(msg: types.Message):
    name = list(msg.text.split())
    
    with open('phonebook.csv', "a", newline='', encoding='utf-8') as bd:
        f_writ = csv.writer(bd, delimiter = ";", lineterminator="\n" )
                   
        f_writ.writerow(name)
        f_writ.writerow(' ')

    
def answer2(msg: types.Message):   
    num = msg.text
    
    with open('phonebook.csv', "r", newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if num == '2':
                item = ', '.join(row)
                bot.send_message(chat_id=msg.from_user.id, text=f'{item}')
            if num == '1':
                for item in row:
                    bot.send_message(chat_id=msg.from_user.id, text=f'{item}')

def answer3(msg: types.Message):
    b = list(msg.text.split())

    file_name_expott = b[0]
    num_exp = b[1]
    if num_exp == '1':
        export_data.export_to_xml(file_name_expott)
        bot.send_document(chat_id=msg.from_user.id, document=open(f'{file_name_expott}.xml', 'rb'))
        
    elif num_exp == '2':
        export_data.csv_to_json(file_name_expott)
        bot.send_document(chat_id=msg.from_user.id, document=open(f'{file_name_expott}.json', 'rb'))
            

def answer4(msg: types.Message):
    ss = list(msg.text.split())
    num = ss[0]
    path = ss[1]
    namee = ss[2]
    if num == '1':
        arr1 = import_data.copy_cont(path, namee)
        import_data.write_csv(arr1)
    if num == '2':
        import_data.copy_cont_json(path, namee)

def answer5(msg: types.Message):
    searchname = msg.text
    se_name = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + se_name
    myfile = open('phonebook.csv', 'r+', encoding='utf-8')
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат {line}')
            
            found = True
            break
    if found == False:
        bot.send_message(chat_id=msg.from_user.id, text=f'Запрашиваемый Вами контакт не найден')

def answer6(msg: types.Message):
    ss = list(msg.text.split())
    num = ss[0]
    path = ss[1]
    
    if num == '1':
        arr1 = import_data.copy_cont1(path)
        import_data.write_csv(arr1)
    if num == '2':
        import_data.copy_cont_json1(path)

# Сохраняем в csv
def save_to_csv(new_contacts, file_name = 'phonebook.csv'):
    with open(file_name, "a", newline='', encoding='utf-8') as bd:
        for i in range(len(new_contacts)):
            if i != len(new_contacts) - 1:
                bd.write(f'{new_contacts[i]};')
            else:
                bd.write(f'{new_contacts[i]}')
        bd.write('\n')

@bot.message_handler(content_types=['document'])
def answer11(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text='док сохранен')

    if 'csv' in filename:
        arr1 = import_data.copy_cont1(filename)
        import_data.write_csv(arr1)
    if 'json' in filename:
        import_data.copy_cont_json1(filename)

    
    

bot.polling()

