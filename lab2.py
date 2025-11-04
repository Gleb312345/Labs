list = [23,4,6,214,5,1236,5,909,12,15,'a','z','x','d','e','o','k','i','u','v']

list_str = [v for v in list if isinstance(v, str)]
list_int = [v for v in list if isinstance(v, int)]
list_int.sort()
list_str.sort()

list_sort = list_int.copy()
list_sort.extend(list_str)

list_2 = []

for n in list_int:
    if n % 2 == 0:
        list_2.append(n)

list_STR = []

for v in list_str:
    list_STR.append(v.upper())

print('Початковий список:',list)
print('Сортований список:',list_sort)
print('Список кратних 2:',list_2)
print('Список капсом:',list_STR)