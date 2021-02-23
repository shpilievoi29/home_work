#Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
from collections import Counter

open_text = open('text_english.txt', 'r')
read_text = open_text.read().lower()
text_string1 = read_text.split()
y = Counter(text_string1)
print(y)
