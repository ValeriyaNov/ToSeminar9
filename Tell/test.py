import csv
from telebot import TeleBot, types
TOKEN = '5615159193:AAFAm4a5YKA3w2EhtlvwS9qkDEzL0jqalUo'
 
bot = TeleBot(TOKEN)

# Создаем новый контакт
def new_contact():
    first_name = input_firstname()
    last_name = input_lastname()
    def answer(msg: types.Message):
        #id_ = msg.from_user.id
        text = msg.text
    
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите второе число')
        return text
    phone_number = answer()
    description = input_description()
    new_list = [first_name, last_name, phone_number, description]
    #save_to_csv(new_list)
    #print('Данные успешно сохранены')


# Вводим имя
def input_firstname():
    def answer(msg: types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=f'Имя!')
        first = msg.text
        return first
    first = answer()
    fi_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + fi_name


# Вводим фимилию
def input_lastname():
    def answer(msg: types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=f'Фамилия!')
        first = msg.text
        return first
    first = answer()
    la_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + la_name


#  Вводим описание
def input_description():
    def answer(msg: types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=f'Описание!')
        first = msg.text
        return first
    first = answer()
    pa_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + pa_name

'''
# Сохраняем в csv
def save_to_csv(new_contacts, file_name = 'phonebook.csv'):
    with open(file_name, "a", newline='', encoding='utf-8') as bd:
        for i in range(len(new_contacts)):
            if i != len(new_contacts) - 1:
                bd.write(f'{new_contacts[i]};')
            else:
                bd.write(f'{new_contacts[i]}')
        bd.write('\n')


# Читаем csv
def read_contact(unit = 1, file_name = 'phonebook.csv'):
    with open(file_name, "r", newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if unit == 2:
                item = ', '.join(row)
                print(item)
            if unit == 1:
                for item in row:
                    print(item)
                print()
'''