# Поиск   Код от Александра
def searchcontact(searchname):
    se_name = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + se_name
    myfile = open('phonebook.csv', 'r+')
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print('Результат поиска: ', end = ' ')
            print( line)
            found = True
            break
    if found == False:
        print('Запрашиваемый Вами контакт не найден...', searchname) 