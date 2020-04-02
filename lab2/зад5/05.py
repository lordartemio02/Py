#Введите с клавиатуры текст. Программно найдите в нем и выведите отдельно все
#слова, которые начинаются с большого латинского символа (от A до Z) и заканчиваются
#2 или 4 цифрами, например «Petr93», «Johnny70», «Service2002».
#Используйте регулярные выражения.
import re
text = input()
#text = 'Petr93 Johnny70 Service2002 Kol111'
pattern = r'\b[A-Z]\w+\D[0-9]{4}\b|\b[A-Z]\w+\D[0-9]{2}\b'
re_text = re.findall(pattern, text)
print(re_text)

