from generator import Generator
from etc import heading, ending
from collections import OrderedDict
from utils import text_file_writer

master = []

def appender(lists):
    for i in lists:
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


heading()
first_name = input('> Firstname: ').lower()
if first_name == '':
    while bool(first_name) != True:
        print('A name is required!!')
        first_name = input('> Name: ').lower()

last_name = input('> Lastname: ').lower()
nick_name = input('> Nickname: ').lower()
birthdate = input('> Birthdate(DDMMYYYY): ')
special = input('\n\n> Do you want special characters in the list?(y/n) ')
keywords = input(
    '> Keywords you might want to include(sperated by a coma, ex:samsepi,mrrobot) ')
key = []
key = keywords.split(',')

if birthdate == '':
    birthdate = 0
else:
    birthdate = int(birthdate)

if special == 'y':
    special = True
else:
    special = False

execution()
# Remove duplicates
master = list(OrderedDict.fromkeys(master))
text_file_writer(first_name, master)
ending(first_name)