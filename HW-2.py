
print('___Задача 1____')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']},
]

rus_geo_logs = list(filter(lambda visit: 'Россия' in list(visit.values())[0], geo_logs))
print(rus_geo_logs)



print('___Задача 2____')
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

uniq = set(list(v for value in ids.values() for v in(value if isinstance(value,list) else [value])))
print(uniq)

print('___Задача 3____')

queries = [

    'смотреть сериалы онлайн',

    'новости спорта',

    'афиша кино',

    'курс доллара',

    'сериалы этим летом',

    'курс по питону',

    'сериалы про спорт',
]


res = {}
for i in queries:
 stats = len(i.split())
 # res[stats] = 0
 if stats in res.keys():
    res[stats] = 1
 else:
     res[stats] = 0
print(res)
#Просила помочь решить эту задачу у аспирантов, они мне сказали составить такой словарь
# Зачем он здесь и как сделать так чтобы он работал, я не понимаю

print('___Задача 4____')

stats = {'facebook': 55,
         'yandex': 120,
         'vk': 115,
         'google': 99,
         'email': 42,
         'ok': 98}


for key in stats:
    i = max(stats.values())
    if stats.get(key) < i:
        continue
    elif stats.get(key) == i:
     print(key)

print('___Задача 5____')


stream = [
	'2018-01-01,user1,3',
	'2018-01-07,user1,4',
	'2018-03-29,user1,1',
	'2018-04-04,user1,13',
	'2018-01-05,user2,7',
	'2018-06-14,user3,4',
	'2018-07-02,user3,10',
	'2018-03-21,user4,19',
	'2018-03-22,user4,4',
	'2018-04-22,user4,8',
	'2018-05-03,user4,9',
	'2018-05-11,user4,11',
]
for i in stream:
 # print(i)
 str = i.split(',')
 looking = (str[2])
 print(looking)
 #Вот удалось вывести все просмотры. Однако сложить их не получается.
 #Предполагала посчитать общуюсумму просмотров вот таким выражением
 # sum(looking) но вы цикле это не работает
 usr_set = (str[1])
 print(usr_set)
 # такая же беда, выражение set(usr_set) в цикле дает не то множество, которе нужно
 # после того, как удастся вывести множество, нужно посчитать его длину, далее разделить
 # looking/usr_set, в цикле

print('___Задача 6____')

stats = [
	['2018-01-01', 'google', 25],
	['2018-01-01', 'yandex', 65],
	['2018-01-01', 'market', 89],
	['2018-01-02', 'google', 574],
	['2018-01-02', 'yandex', 249],
	['2018-01-02', 'market', 994],
	['2018-01-03', 'google', 1843],
	['2018-01-03', 'yandex', 1327],
	['2018-01-03', 'market', 1764],
]

for i in stats:
  x = i[2]
  # print(i[1])
  y = '2018-01-03', 'market'
  if y == i[0] and y == i[1]:
      print(x)
  else:
      print('Error')

#Предполагала решить это так, но скрипт выдает ошибку

