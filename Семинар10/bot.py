import telebot
import crud as cr
import logger as lg


token = cr.get_token()
bot = telebot.TeleBot(token, parse_mode='MARKDOWN')


@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(
        message.chat.id, f'Я тебя не понимаю. Введи: /help.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, *{message.from_user.first_name}!*\nВ любой непонятной ситуации введи\nкоманду: /help\nДа! кнопки скоро появятся ;)\nЧтобы вызвать главное меню введи: /main')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - начать сначала (перезапустить бота)\n/main - главное меню\n/help - вызвать справку')


name_it = ''
surname_it = ''
number_it = ''
email_it = ''
user_id_it = ''
new_number_it = ''


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/main':
        bot.send_message(message.chat.id, f'Выбери пункт меню, введя соответствующую команду: \n/1 - Показать все записи.\n/2 - Найти номер по фамилии.\n/3 - Найти номер по имени.\n/4 - Поиск по номеру телефона.\n/5 - Добавить новую запись.\n/6 - Изменить существующую запись.\n/7 - Удалить запись.\n/8 - Курсы валют.')
        cr.init_data_base('base_phone.csv')

    elif message.text == '/1':
        lg.logging.info('The user has selected item number 1')
        bot.send_message(message.chat.id, f'{cr.retrive()}')

    elif message.text == '/2':
        lg.logging.info('The user has selected item number 2')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, find_surname)

    elif message.text == '/3':
        lg.logging.info('The user has selected item number 3')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, find_name)

    elif message.text == '/4':
        lg.logging.info('The user has selected item number 4')
        bot.send_message(message.chat.id, f'Введите номер  телефона')
        bot.register_next_step_handler(message, find_number)

    elif message.text == '/5':
        lg.logging.info('The user has selected item number 5')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, get_name)

    elif message.text == '/6':
        lg.logging.info('The user has selected item number 6')
        bot.send_message(
            message.chat.id, f'Какой контакт хотите изменить?\nУкажите по:\n/61 - Фамилии\n/62 - Имени\n/63 - Номеру телефона')
        bot.register_next_step_handler(message, edit_entry)

    elif message.text == '/7':
        lg.logging.info('The user has selected item number 7')
        bot.send_message(
            message.chat.id, f'Выберите контакт, который хотите удалить?\nВыберите по:\n/71 - Фамилии\n/72 - Имени\n/73 - Номеру телефона')

    elif message.text == '/8':
        lg.logging.info('The user has selected item number 8')
        bot.send_message(
            message.chat.id, f'Узнать курс валют\nВыберите:\n/81 - Список кодов валют\n/82 - Курс валюты к долару США')
        bot.register_next_step_handler(message, find_cur)

    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /help.')


def find_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')


def find_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')


def find_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')


def get_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'Введите фамилию')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'Введите номер телефона')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'Введите электронную почту')
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    global email_it
    email_it = message.text
    lg.logging.info('User entered: {email_it}')
    cr.create(name_it, surname_it, number_it, email_it)
    bot.send_message(message.chat.id, f'Контакт успешно добавлен!')


def edit_entry(message):
    if message.text == '/61':
        lg.logging.info('The user has selected item number 6.1')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, change_surname)

    elif message.text == '/62':
        lg.logging.info('The user has selected item number 6.2')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, change_name)

    elif message.text == '/63':
        lg.logging.info('The user has selected item number 6.3')
        bot.send_message(message.chat.id, f'Введите номер телефона')
        bot.register_next_step_handler(message, change_num)

    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /help.')


def change_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите изменить')
    bot.register_next_step_handler(message, change_number)


def change_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите изменить')
    bot.register_next_step_handler(message, change_number)


def change_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите изменить')
    bot.register_next_step_handler(message, change_number)


def change_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    bot.send_message(
        message.chat.id, f'Введите новый номер телефона')
    bot.register_next_step_handler(message, change_new_number)


def change_new_number(message):
    global new_number_it
    new_number_it = message.text
    lg.logging.info('User entered: {new_number_it}')
    cr.update(id=user_id_it, new_number=new_number_it)
    bot.send_message(
        message.chat.id, f'Контакт успешно изменен!')


def delete_contact(message):
    if message.text == '/71':
        lg.logging.info('The user has selected item number 7.1')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, delete_surname)

    elif message.text == '/72':
        lg.logging.info('The user has selected item number 7.2')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, delete_name)

    elif message.text == '/73':
        lg.logging.info('The user has selected item number 7.3')
        bot.send_message(message.chat.id, f'Введите номер телефона')
        bot.register_next_step_handler(message, delete_num)

    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /help.')


def delete_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите удалить')
    bot.register_next_step_handler(message, delete_number)


def delete_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите удалить')
    bot.register_next_step_handler(message, delete_number)


def delete_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите удалить')
    bot.register_next_step_handler(message, delete_number)


def delete_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    cr.delete(id=user_id_it)
    bot.send_message(
        message.chat.id, f'Контакт успешно удален!')

def find_cur(message):
    if message.text == '/81':
        lg.logging.info('The user has selected item number 8.1')
        bot.register_next_step_handler(message, change_surname)
        bot.send_message(message.chat.id, f'{cr.currency(id=1, cur_name="")}')
        #items = cr.currency(id=1, cur_name='')
        #for key, value in items:
        #    bot.send_message(message.chat.id, (key+'-'+value))

    elif message.text == '/82':
        lg.logging.info('The user has selected item number 8.2')
        bot.send_message(message.chat.id, f'Введите коды валют (можно через запятую)')
        bot.register_next_step_handler(message, find_curs)

    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /help.')

def find_curs(message):
    global cur_name
    cur_name = message.text
    lg.logging.info('User entered: {user_id_it}')
    bot.send_message(message.chat.id, f'{cr.currency(id=2, cur_name=cur_name)}')
    #items = cr.currency(id=2, cur_name=cur_name)
    #for key, value in items:
    #    bot.send_message(message.chat.id, (key + ' - ' + str(round(value, 2))))


print('server start')
bot.infinity_polling()