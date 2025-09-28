

class Product:
    def __init__(self,name,price,quantity):
        self.name= name
        self.price = price
        self.quantity = quantity
class Shop:
    def __init__(self):
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)
        print(f'{product.name} product is add in the list')
    def buy_product(self,product_name,quantity):
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"Congratulations! You have successfully bought {quantity} {product.name}(s).")
                    return
                else:
                    print(f"Sorry! Not enough stock of {product.name}.")
                    return
        print(f"Sorry! {product_name} is not available in the shop.")

p1 = Product("Apple", 50, 10)
p2 = Product("Orange", 40, 5)

my_shop = Shop()

my_shop.add_product(p1)
my_shop.add_product(p2)

my_shop.buy_product('Apple', 5)
my_shop.buy_product('Orange',10)
my_shop.buy_product('banana',3)
print()

#Inheritance
class Animal:
    def sound(self):
        print('animals amke sounds')
class Dog(Animal):
    def sound(self):
        print('dog barks')
class Cat (Animal):
    def sound(self):
        print('caar meows')

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
print()

#Encapsulation
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self, amount) :
        self.balance += amount
    def withdraw(self ,amount):
        if amount <=self.balance:
            self.balance -= amount
            print()
        else:
            print("Insufficient funds!")
    def get_balance(self):
        return self.balance

BA = BankAccount(10000)
BA.deposit(1000)
BA.withdraw(2000)
print(BA.get_balance())
 
#abestraction
class Example:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

obj = Example()
print(obj.public)       
print(obj._protected)   
#print(obj.__private) 

name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age)) 

                  
    

        