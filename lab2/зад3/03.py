#Задан путь к директории с музыкальными файлами
#(в названии которых нет номеров, а только названия песен)
#и текстовый файл, хранящий полный список песен с номерами
#и названиями в виде строк формата «01. Freefall [6:12]».
#Напишите скрипт, который корректирует имена файлов в директории
#на основе текста списка песен.
import os
import re
Play_List = {}
path_directory = os.getcwd()
print(path_directory)
f= open (r'Play_List.txt')
lines = f.readlines()
f.close()
pattern_number = r'(\d+\.\s)[\w\s-]+'
pattern_name = r'\d+\.\s([\w\s-]+)'
for line in lines:
    re_num = ''.join(re.findall(pattern_number, line))
    re_name =''.join(re.findall(pattern_name, line)).rstrip()
    Play_List[re_name] = re_num
print(Play_List)
print(os.listdir(path_directory))
for name in os.listdir(path_directory):
    if name.endswith('.mp3') and name[:-4] in Play_List :
        os.rename(name, Play_List[name[:-4]]+name)
        print('do this')
        
#Сдать
