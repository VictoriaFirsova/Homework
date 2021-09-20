# Task 1.4
# Write a Python program to sort a dictionary by key.
my_dict = {'марафон': 'гонка бегунов длиной около 26 миль',   # Если ключи однотипные
           'персона': 'человек',
           'бежал': 'бежать в прошедшем времени',
           'бежать': 'двигаться со скоростью',
           'туфля': 'род обуви, закрывающей ногу не выше щиколотки',
           'туфли': 'туфля во множественном числе'}
sorted_keys = sorted(my_dict.keys())
sorted_dict = {i: my_dict.get(i) for i in sorted_keys}
print(sorted_dict)

my_dict2 = {456123: 'гонка бегунов длиной около 26 миль',   # Если ключи int, str и tuple
            789: 'человек',
            (5, 7, 8): 'бежать в прошедшем времени',
            (2, 3, 4): 'двигаться со скоростью',
            'туфля': 'род обуви, закрывающей ногу не выше щиколотки',
            'туфли': 'туфля во множественном числе'}
str_keys = []
int_keys = []
tuple_keys = []
for key in my_dict2.keys():
    if type(key) == tuple:
        tuple_keys.append(key)
    elif type(key) == int:
        int_keys.append(key)
    elif type(key) == str:
        str_keys.append(key)
str_keys.sort()
int_keys.sort()
tuple_keys.sort()
sorted_keys2 = str_keys+int_keys+tuple_keys
sorted_dict2 = {i: my_dict2.get(i) for i in sorted_keys2}
print(sorted_dict2)