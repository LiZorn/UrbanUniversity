from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self): #то, как данные будут выглядеть в терминале
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
        __file_name = "products.txt" #инкапсулированный или приватный атрибут, используемый только в классе
    def get_products(self):
        opener = open(self.__file_name, 'r')
        text = opener.read()
        opener.close()
        return text

    def add(self, *products):
        products_in_file = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in products_in_file:
                file.write(str(product) + "\n")
                products_in_file += str(product)
            else:
                print(f'Продукт {product} уже есть в магазине.')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
