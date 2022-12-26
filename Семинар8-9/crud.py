import csv
import os.path
import logger as lg


db_file_name = ''
db = []
global_id = 0  # id для добавления пользователей


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower()):
            print("уже существует")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number, email.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


# поиск (если нужно выгрузить все: result = retrive())
def retrive(id='', name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        if(email != '' and row[3] != email.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        # выход список списков (переделать в строку с разделителем)
        #return result
        str = ''
        for item in result:
            #print(' '.join(item))
            str = str + ' '.join(item) + '\n'
        return str



def update(id='', new_name='', new_surname='', new_number='', new_email=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_surname != ''):
                    row[2] = new_surname.title()

                if(new_number != ''):
                    row[3] = new_number
                if(new_email != ''):
                    row[3] = new_email.lower()

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def get_token():
    file = open('token.csv', 'r')
    for i in file:
        token = i
    file.close()
    return token


def export(id, file_name):
    global global_id
    global db
    global db_file_name
    if id == 1:
        with open(file_name, 'w') as data:
            for item in db:
                for rec in item:
                    data.write(f"{rec}\n")
                data.write(f"\n")
    elif id == 2:
        with open(file_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';',
                                quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            for item in db:
                writer.writerow(item)
    return

def import_file(id, file_name):
        global global_id
        global db
        global db_file_name
        if id == 1:
            #with open(file_name, 'r') as f:
                #nums = ''
                #numss = []
                #nums = f.readline()#.split("\n")
                #nums = nums + f.readline()
                #nums = nums + f.readline()
                #nums = nums + f.readline()
                #nums = nums + f.readline()
                #numss = nums.split("\n")
                #print(nums)
            # получим объект файла
            file1 = open(file_name, "r")
            # считываем все строки
            lines = file1.readlines()
            # итерация по строкам
            i = 0
            l = []
            for line in lines:
                i = i + 1
                if i == 6:
                    db.append(l)
                    with open(db_file_name, 'a', newline='') as csv_file:
                        writer = csv.writer(csv_file, delimiter=';',
                                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(l)
                    l = []
                    i = 0
                else:
                    l.append(line.replace("\n",""))
            # закрываем файл
            file1.close
        elif id == 2:
            with open(file_name, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=';',
                                    quotechar='\'', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    if (row[0] != 'ID'):
                        db.append(row)
                        with open(db_file_name, 'a', newline='') as csv_file:
                            writer = csv.writer(csv_file, delimiter=';',
                                                quotechar='\'', quoting=csv.QUOTE_MINIMAL)
                            writer.writerow(row)
                        if (int(row[0]) > global_id):
                            global_id = int(row[0])
        return

    # ====================ВНИМАНИЕ ПРИМЕР ИСПОЛЬЗОВАНИЯ НИЖЕ=======================
    # init_data_base("test.csv") # инициализация базы

    # =================Примеры создания записей=================
    # create('vasya','pupkin','123', 'email@email.com')
    # create('vasya','pupkin','123', 'emaasd@email.com')
    # create('vasya','pupkin','1232432', 'emgg54l@email.com')
    # create('vasya','pupkin','1', 'emb@email.com')
    # create('vasya','pup','123', 'email@email.com')
    # create('vas1','123')

    # ==================Примеры поиска записей===============
    # print(retrive()) # Выбор всего что есть
    # print(retrive(number='123'))
    # print(retrive(id='123'))
    # print(retrive(id='1', number='123'))

    # ==================Обновление записи==================
    # update(id='2', new_number='09876544', new_name='petya')

    # ===================Удаление записи=======================
    # delete('1')