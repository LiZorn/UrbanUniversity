my_dict={'Liza':1999,'Jan':1991,'Nat':1975}
print(my_dict)
print(my_dict["Liza"])
print(my_dict.get('Denis'))
my_dict.update({'Sasha':1998,
                'Nastya':1990})
a = my_dict.pop('Sasha')
print(a)
del my_dict["Liza"]
print(my_dict)

my_set={"Sasha", 1, 1, 2, 2, 3, 3.456}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.remove(3.456)
print(my_set)
