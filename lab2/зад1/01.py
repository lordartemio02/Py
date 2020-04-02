#Напишите скрипт, который читает текстовый файл и
#выводит символы в порядке убывания частоты встречаемости
#в тексте. Регистр символа не имеет значения. Программа
#должна учитывать только буквенные символы (символы
#пунктуации, цифры и служебные символы слудет игнорировать).
#Проверьте работу скрипта на нескольких файлах с текстом на
#английском и русском языках, сравните результаты с таблицами,
#приведенными в wikipedia.org/wiki/Letter_frequencies.

filename_en = open('text_en.txt', 'r')
text_en = filename_en.read()
text_en = text_en.lower()
filename_ru = open('text_ru.txt', 'r')
text_ru = filename_ru.read()
text_ru = text_ru.lower()
print("Количество русских букв " + str(len(text_ru)))
print("Количество англ букв " + str(len(text_en)))
english = 'abcdefghijklmnopqrstuvwxyz'
russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
liters_count_ru = {russian[i]: text_ru.count(russian[i]) for i in range(len(russian))}
liters_count_en = {english[i]: text_en.count(english[i]) for i in range(len(english))}
print( str(sorted(liters_count_ru.items(), key=lambda x: x[1], reverse=True)) + "\n")
print( sorted(liters_count_en.items(), key=lambda x: x[1], reverse=True) )
