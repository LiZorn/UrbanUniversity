def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 'строка')
print_params(1,25, True)
print_params(1,25, [1,2,3])

values_list = [1, 'pop', False]
values_dict = {"a": True, "b": 2, "c": 'star'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["fufu", 0]
print_params(*values_list_2, 42)

