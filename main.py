# словари и множества
my_dict={'Лена': 1986,'Алексей': 1985,'Cафия': 2017}
print('словарь:',my_dict)
my_dict['Лена']= 2000
print(my_dict)
my_dict['Маша']=1987
print(my_dict)
my_dict.update({'Лера':  1243,'Миша': 1985})
a= (my_dict.pop('Алексей'))
print('Вывод значения удаленного ключа:',a)
print('Измененный словарь:', my_dict)


# работа с множеством
my_set={2,2,23,3,3,4,5,6,6,True,True,True,set,list,list}
print('Множество:',my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:',my_set)