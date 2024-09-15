from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        self.opener = open(self.__file_name, 'r')
        return self.opener.read()
        file.close()

    def get_product_names(self):
        file = open(self.__file_name, 'r')
        lines = file.readlines()
        products_name = []
        for line in lines:
            products_name.append(line.split(', ')[0])
        file.close()
        return products_name

    def add(self, *products):
        for i in products:
            self.opener = open(self.__file_name, 'r')
            if i.name not in self.opener.read():
                self.opener = open(self.__file_name, 'a')
                self.opener.write(f'{i}\n')
                self.opener.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине.')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
