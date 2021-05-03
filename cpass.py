from generator import Generator
from etc import heading, ending
from collections import OrderedDict
from utils import text_file_writer, appender

master = []

def execution():
    f = Generator(first_name, special)
    appender(f.result(), master)
    if bool(last_name) == True:
        unprocessed_words = [last_name, first_name+last_name, last_name+first_name]
        for item in unprocessed_words:
            l = Generator(item, special)
            appender(l.result(), master)
    if bool(nick_name) == True:
        unprocessed_words = [nick_name, first_name+nick_name, nick_name+first_name]
        for item in unprocessed_words:
            n = Generator(item, special)
            appender(n.result(), master)
    if birthdate != 0:
        words = [first_name, last_name, nick_name]
        for name in words:
            n = Generator(name, special)
            appender(n.birthday(birthdate), master)
    if bool(keywords) == True:
        for word in key:
            k = Generator(word, special)
            appender(k.result(), master)


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