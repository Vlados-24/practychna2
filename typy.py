str_var = "Hello world!"
int_var = 23
float_var = 3
bool_var = False
list_var = [1, 2, 3, "car"]
dict_var = {"name": "Max", "age": 32}
tuple_var = (10, 20, 30)
none_var = None

print(int_var > float_var)
print(int_var == 23) 
print("car" > "bus")
print(bool_var == True)
print(bool_var != False)
print(list_var == [1, 2, 3, "car"])
print(list_var is [1, 2, 3, "car"])
print(dict_var == {"name": "Max", "age": 32})
print(dict_var is {"name": "Max", "age": 32})
print(tuple_var == (10, 20, 30))
print(tuple_var is (10, 20, 30))
print(len(str_var))
print(abs(-15))
print(round(float_var))
print(sum(tuple_var))
print(list_var.append("new item"))
print(dict_var.get("name"))
print(type(bool_var))
print(sorted([3, 1, 4, 1, 5, 9]))

split_test = 'Hi, my name is Python!'
split_list = split_test.split()
print("Список слів:", split_list)
string_join = ' '.join(split_list)
print("Об'єднаний рядок:", string_join)
length = len(string_join)
print("Довжина рядка:", length)
length = len(string_join)
print(length)

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print("Оновлений list_append:", list_append)
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print("Оновлений list_extend:", list_extend)
index_6 = list_extend.index(6)
print("Індекс елемента 6:", index_6)
length_list_append = len(list_append)
print("Довжина list_append:", length_list_append)

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print("Car:", dict_test['car'])  
print("Where:", dict_test['where'])
print("Keys:", dict_test.keys())
print("Values:", dict_test.values())
print("Items:", dict_test.items())