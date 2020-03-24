
# Напишите скрипт, который преобразует введенное с клавиатуры
# вещественное число в денежный формат. Например, число 12,5 должно
# быть преобразовано к виду «12 руб. 50 коп.». В случае ввода
# отрицательного числа выдайте сообщение «Некорректный формат!»
# путем обработки исключения в коде

# print("Print your money (float)")
# money = float(input())
# def money_convert(money):
#         if money < 0.0:
#                 raise
#         else:
#                 return'{}руб.{}коп.'.format(int(money), int((money-int(money))*100))
# try:
#     print(money_convert(money))

# except:
#     print('Некоректный ввод')


# Написать скрипт, который выводит на экран «True», если элементы
# программно задаваемого списка представляют собой возрастающую
# последовательность, иначе – «False»



# def check(arr):
#     for i in range(1, len(arr)):
#         if arr[i]<arr[i-1]:
#             return False
#     return True
# list_one = [1, 2, 3]
# list_two = [1, 2, 3]
# print(check(list_one))
# print(check(list_two))


#Напишите скрипт, который позволяет ввести с клавиатуры номер дебетовой карты
#16 цифр) и выводит номер в скрытом виде: первые и последние 4 цифры отображены
#нормально, а между ними – символы «*» (например, 5123 **** **** 1212).

# def number_convert(number):
#     print(*mass[:4],'****', '****',*mass[12:16])
# print('Пример ввода :5123 0000 0000 1212')
# mass = []
# try:
#     number = input().replace(' ', '')
#     for i in range(len(number)):
#         if number[i].isdigit() == True and len(number) > 16:
#             mass.append(number[i])
#         else:
#             raise
#     number_convert(number)  
# except:
#     print('Данный формат не соответсвует норме!')


#Напишите скрипт, который разделяет введенный с клавиатуры текст на слова
#и выводит сначала те слова, длина которых превосходит 7 символов, затем
#слова размером от 4 до 7 символов, затем – все остальные.


# text = input()
# more_7=[]
# between_4and7=[]
# less_4=[]
# def conver_text_str(text):
#     word=text.split()
#     for i in range (len(word)):
#         if len(list(word[i]))>7:
#             more_7.append(word[i])
#         elif len(list(word[i]))>4 and len(list(word[i]))<7:
#             between_4and7.append(word[i])
#         else:
#             less_4.append(word[i])
#     print(more_7)
#     print(between_4and7)
#     print(less_4)
# conver_text_str(text)



#Напишите скрипт, который позволяет ввести с клавиатуры текст
#предложения и сформировать новую строку на основе исходной, в
#которой все слова, начинающиеся с большой буквы, приведены к
#верхнему регистру. Слова могут разделяться запятыми или пробелами.
#Например, если пользователь введет строку «город Донецк, река Кальмиус»,
#результирующая строка должна выглядеть так: «город ДОНЕЦК, река КАЛЬМИУС».
#text = "город Донецк, река Кальмиус"
# text = input()
# def change_registr(text):
#     word = text.split()
#     for i in range (len(word)):
#         if(word[i].istitle()):
#             print (word[i].upper(), end=' ')
#         else:
#             print(word[i], end = ' ')
# change_registr(text)
#Напишите скрипт, который обрабатывает список строк-адресов
#следующим образом: сначала определяет, начинается ли каждая
#строка в списке с префикса «www». Если условие выполняется,
#то скрипт должен вставить в начало этой строки префикс
#«http://», а затем проверить, что строка заканчивается на
#«.com». Если у строки другое окончание, то скрипт должен
#вставить в конец подстроку «.com». В итоге скрипт должен
#вывести на консоль новый список с измененными адресами.
#Используйте генераторы списков.

# adress = ['www.google.ru','google.com','google.ru']
# def change_adress (adress):
#     for i in range (len(adress)):
#         if adress[i].startswith('www.'):
#             adress[i] = 'http://' + adress[i]
#         if adress[i].endswith('.com')== False:
#             adress[i] = adress[i] + '.com'
#         print (adress[i])
# change_adress(adress)


#Напишите скрипт, генерирующий случайным образом число n в диапазоне от 1 до 10000.
#Скрипт должен создать массив из n целых чисел, также сгенерированных случайным
#образом, и дополнить массив нулями до размера, равного ближайшей сверху степени
#двойки. Например, если в массиве было n=100 элементов, то массив нужно дополнить
#28 нулями, чтобы в итоге был массив из 28=128 элементов (ближайшая степень двойки
#к 100 – это число 128, к 35 – это 64 и т.д.).
# import random
# def raandoom(n):
#     i = 0
#     while i < n:
#         yield random.randint(1, 100)
#         i += 1
# n =random.randint(1,100)


# array = list(raandoom(n))
# for i in range(n):
#     if i**2 > n:
#         ziro = [0 for ziro  in range(i**2)]
#         array.extend(ziro)
#         break
# print(array)
# print(len(array))
#Напишите программу, имитирующую работу банкомата. Выберите структуру данных для хранения
#купюр разного достоинства в заданном количестве. При вводе пользователем запрашиваемой
#суммы денег, скрипт должен вывести на консоль количество купюр подходящего достоинства.
#Если имеющихся денег не хватает, то необходимо напечатать сообщение «Операция не может
#быть выполнена!». Например, при сумме 5370 рублей на консоль должно быть выведено
#«5*1000 + 3*100 + 1*50 + 2*10». 
moneybank = {1000: 6, 500: 6, 200: 1, 100: 10, 50: 10, 10: 1}
result = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 10: 0}
outputmoney = ""
money = 5360
checkmoney = 0
for i in moneybank.keys():
    checkmoney += moneybank[i] * i
    current = money // i  # деление без остатка
    if current > moneybank[i]:
        money = money - (moneybank[i] * i)
        print(money)
        result[i] = moneybank[i]
    else:
        money = money % i
        result[i] = current   
if checkmoney < money  or money > 0:
    print("Операция не может быть выполнена!")
else:
    for i in result.items():
        if i[1] != 0:
            outputmoney += str(i[1]) + " * " + str(i[0]) + " + "
    print(outputmoney[:-2])



#Напишите скрипт, позволяющий определить надежность вводимого
#пользователем пароля. Это задание является творческим: алгоритм
#определения надежности разработайте самостоятельно.
# password = input()
# symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}']
# count_num = 0
# count_sym = 0
# count_upp = 0
# numeric=0
# numsymbols=0
# upper=0
# crash_pass=list(password)
# pwlength = len(password)
# for i in range (len(crash_pass)):
#     if crash_pass[i].isdigit():
#         count_num +=1
#     if crash_pass[i].isupper():
#         count_upp+=1
#     for j in range (len(symbols)):
#         if crash_pass[i]==symbols[j]:
#             count_sym+=1
# numeric = count_num
# numsymbols = count_sym
# upper = count_upp
# print(pwlength)
# print(numeric)
# print(numsymbols)
# print(upper)
# pwstrength = ((pwlength*10)-20)+(numeric*10)+(numsymbols*15)+(upper*10)
# if pwstrength>100:
#     pwstrength = 100
# elif pwstrength<0:
#     pwstrength = 0 
# print(pwstrength)

#Напишите генератор frange как аналог range() с дробным шагом. Пример вызова:
#for x in frange(1, 5, 0.1):
#    print(x) # выводит 1 1.1 1.2 1.3 1.4 … 4.9

# def frange (start, end, step):
#     for i in range(start, end):
#         while i < end:
#             i+=step
#             yield i
# for x in frange (1, 5, 0.1):
#     print(x)


#Напишите генератор get_frames(), который производит «оконную
#декомпозицию» сигнала: на основе входного списка генерирует набор
#списков – перекрывающихся отдельных фрагментов сигнала размера
#size со степенью перекрытия overlap. Пример вызова:
#for frame in get_frames(signal, size=1024, overlap=0.5):
#   print(frame)

# signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def get_frames(signal, size, overlap):
#     size = size*overlap
#     start = 0
#     end = int(size)
#     while end<=len(signal):
#         frame = signal[start:end]
#         yield frame
#         start+=int(size)
#         end += int(size)
        
# for frame in get_frames (signal, size = 8, overlap = 0.5):
#     print (frame)


#Напишите собственную версию генератора enumerate под названием
#extra_enumerate. Пример вызова:
#for i, elem, cum, frac in extra_enumerate(x):
#   print(elem, cum, frac)
#В переменной cum хранится накопленная сумма на момент текущей
#итерации, в переменной frac – доля накопленной суммы от общей
#суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
#вывод будет таким:
#(1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)
# x = [1, 3, 4, 2]
# def extra_ennymerate(x):
#     fraction = 0
#     cum=0
#     for step in x:
#         fraction += step
#     for i in range(len(x)):
#         elem = x[i]
#         cum += x[i]
#         frac = cum/fraction
#         yield i, elem , cum , frac
# for i, elem, cum, frac in extra_ennymerate(x):
#     print(elem, cum, frac)


    #Напишите декоратор non_empty, который дополнительно проверяет
#списковый результат любой функции: если в нем содержатся пустые
#строки или значение None, то они удаляются. Пример кода:
#@non_empty
#def get_pages():
#    return ['chapter1', '', 'contents', '', 'line1']
# def non_empty(funk):
#     def wrapper():
#         res = funk()
#         count = 0
#         for i in res:
#             if i == '' or i == None:
#                 res.pop(count)
#             count+=1
#         return res
#     return wrapper

# @non_empty
# def get_pages():
#     return ['chapter1', '', 'contents', '', 'line1']

# print(get_pages())



#Напишите параметризированный декоратор pre_process, который осуществляет предварительную
#обработку (цифровую фильтрацию) списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а
#можно задать в коде (по умолчанию равен 0.97). Пример кода:
#@pre_process(a=0.93)
#def plot_signal(s):
#    for sample in s:
#        print(sample)

# def pre_process(a=0.97):
#     def deckor(func):
#         def wrapper():
 
#             for i in range(len(s)):
#                 s[i] =s[i]- a * s[i - 1]
#         return wrapper
#     return deckor

# @pre_process(a=0.93)
# def plot_signal(s):
#     for sample in s:
#         print(sample)

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# plot_signal(data)



#Напишите скрипт, который на основе списка из 16 названий
#футбольных команд случайным образом формирует 4 группы по 4
#команды, а также выводит на консоль календарь всех игр (игры
#должны проходить по средам, раз в 2 недели, начиная с 14 сентября
#текущего года). Даты игр необходимо выводить в формате «14/09/2016,
#22:45». Используйте модули random и itertools.
# import random
# import itertools
# import datetime
# n =random.randint(0,15)
# twins=[]
# print(n)
# teams = ['Барселона','Реал Мадрид','Манчестер Юнайтед','Ювентус', 'Бавария', 'Галатасарай', 'Милан', 'Ливерпуль', 'Интер', 'Марсель', 'Фенербахче', 'Арсенал', 'Боруссия', 'Челси', 'Лион', 'Шааахтеер']
# #random.shuffle(teams)
# start = 0
# end = 2
# count=0
# while end<=len(teams):
#     twins += list(teams[start:end]) #Как наполнить твинс срезами?
#     start+=2
#     end+=2
#     print(twins)
# print(twins)
# #разделяю на 4 блока, сплитом
# date_game_start = datetime.datetime(2016, 9, 14, 22, 45)
# i=0
# while i < 8:
#     date_game_next = datetime.timedelta(days=14)
#     date_game = date_game_start+date_game_next
#     date_game_start = date_game
#     print(date_game.strftime("%d/%m/%Y, %H:%M"))
#     i+=1

