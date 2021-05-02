from util import Generator
from collections import OrderedDict


first_name = input('> Firstname: ').lower()
if first_name == '':
    while bool(first_name) != True:
        print('A name is required!!')
        first_name = input('> Name: ').lower()
last_name = input('> Lastname: ').lower()
nick_name = input('> Nickname: ').lower()
birthdate = input('> Birthdate(DDMMYYYY): ')
if birthdate == '': birthdate = 0
else: birthdate = int(birthdate)
special = input('\n\n\n> Do you want special characters in the list?(y/n)')
keywords = input('> Keywords you might want to include(sperated by a coma, ex:chucker,goodfellow)')
key = []
key = keywords.split(',')
if special == 'y':  special = True
else: special = False

master = []

def appender(list):
    for i in list:
        master.append(i)
    return master

def execution():
    f = Generator(first_name, special)
    appender(f.result())
    if bool(last_name) == True:
        l = Generator(last_name, special)
        appender(l.result())
        name = last_name+first_name
        l2 = Generator(name, special)
        appender(l2.result())
        name = first_name+last_name
        l3 = Generator(name, special)
        appender(l3.result())
    if bool(nick_name) == True:
        n = Generator(nick_name, special)
        appender(n.result())
        name = nick_name+first_name
        n2 = Generator(name, special)
        appender(n2.result())
        name = first_name+nick_name
        n3 = Generator(name, special)
        appender(n3.result())
    if birthdate != 0:
        words = [first_name, last_name, nick_name]
        for name in words:
            n = Generator(name, special)
            appender(n.birthday(birthdate))
    if bool(keywords) == True:
        for word in key:
            k = Generator(word, special)
            appender(k.result())
    

def text_file_writer(master):
    with open(f'{first_name}.txt', 'w') as f:
        for item in master:
            f.write(f"{item}\n")

execution()
master = list(OrderedDict.fromkeys(master))
text_file_writer(master)
# print(master)

