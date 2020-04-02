#Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла,
#найти в нем с помощью регулярных выражений все подстроки определенного вида,
#в соответствии с вариантом. Например, для варианта № 1 скрипт должен вывести
#на экран следующее:
#Вариант 3: найдите все IPv4-адреса – подстроки вида «192.168.5.48»

import re
def pattern_srch(lines):
    pattern = r'\d\d\d.\d\d\d.\d.\d\d+'
    count = 0
    for line in lines:
        count+=1
        time = re.findall(pattern, line)
        if time:
            for new_time in time:
                print('Строка {0}, позиция {1} : найдено {2}'.format(count, line.index(new_time), new_time))
file_name = input("Введите название текстового файла - такого вида 'Name.txt': ")
try:
    file = open(file_name)
    lines = file.readlines()
    pattern_srch(lines)
except Exception:
    print('Такого файла не существует!')