
# coding: utf-8
#work1
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
len('Насколько проще было бы писать программы, если бы не заказчики')
print(len(long_phrase))
if (len(long_phrase)) > (len(short_phrase)):
    print('True')
else:
    print('False')
# work2
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
count_symbol_a = text.count('а')
count_symbol_i = text.count('и')
if count_symbol_a > count_symbol_i:
    print('Буква "а" встречается чаще')
else:
    print('Буква "и" встречается чаще')
#work 3
import math
file_size_in_bytes = 1048576
file_size_in_mb = 1048576/math.pow(1024, 2)
print('Объем файла равен', file_size_in_mb, 'Mb')
#work 4
corner_sin = math.sin(30)
print(corner_sin)
#work 5
print(0.1+0.2)
#результат не точный, потому что компьютеры работают в двоичном коде и из-за этого числа с плавающей запятой могут работать не корректно.
#на stack owerflow советуют складывать так, но это тоже не работает почему то:
print(round(0.1, 1) + (round(0.2, 1)))
#work6
a = 10
b = 20
a, b = b, a
print(a)
print(b)

#work7
num = 10011
number = 0
for i in range(len(str(num))):
    number = number + int(str(num)[i])*(2**(len(str(num))-i-1))
print('Число в двоичной форме {} = {}'.format(num, number))
