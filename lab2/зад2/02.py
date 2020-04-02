#Напишите скрипт, позволяющий искать в заданной директории и в
#ее подпапках файлы-дубликаты на основе сравнения контрольных
#сумм (MD5). Файлы могут иметь одинаковое содержимое, но
#отличаться именами. Скрипт должен вывести группы имен
#обнаруженных файлов-дубликатов.
# -*- coding: cp1251 -*-
import os
import hashlib

def walk(dir, dictionary_dople):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path):
      filename = open(path, 'r')
      text = filename.read().encode('utf-8')
      checksum = hashlib.md5(text).hexdigest()
      if checksum in sum_dict:
        sum_dict[checksum]+=[path]
      else:
        sum_dict[checksum]=[path]
      filename.close()
    else:
      walk(path,  dictionary_dople)
  return dictionary_dople
sum_dict = {}
walk(os.getcwd(), sum_dict)
sum_dict = {sum: group for sum, group in sum_dict.items() if len(group) > 1}
counter = 1
for group in sum_dict.values():
    print('Group {}:'.format(counter))
    for path in group:
        print(path)
    counter += 1
    


