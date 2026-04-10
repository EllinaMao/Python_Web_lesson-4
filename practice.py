from decorate import line
from try_catch import TryCatch
from functools import update_wrapper, wraps
from types import MethodType
from colorama import init, Fore
init(autoreset=True)

# 1. Створіть базовий клас Engine, який буде відповідати за керування двигуном:
# Метод start_engine() повинен виводити повідомлення "Engine started".
# Метод stop_engine() повинен виводити повідомлення "Engine stopped".

class Engine:
    '''
    1. Створіть базовий клас Engine, який буде відповідати за керування двигуном:
    Метод start_engine() повинен виводити повідомлення "Engine started".
    Метод stop_engine() повинен виводити повідомлення "Engine stopped".
    
    Engine
    |
    '''
    def start_engine(self):
        print(Fore.CYAN + "Engine started")
    
    def stop_engine(self):
        print(Fore.CYAN + "Engine stopped")


# Створіть базовий клас Vehicle, який буде містити загальні властивості та методи для транспорту:
# Атрибут max_speed для зберігання максимальної швидкості.
# Метод drive() повинен виводити повідомлення "Driving at maximum speed of {max_speed}".

class Vehicle(Engine):
    '''
    2. Створіть базовий клас Vehicle, який буде містити загальні властивості та методи для транспорту:
    Атрибут max_speed для зберігання максимальної швидкості.
    Метод drive() повинен виводити повідомлення "Driving at maximum speed of {max_speed}".

    
    Engine
    |
    |
    Vehicile
    '''
    def __init__(self, max_speed: float):
        self.max_speed = max_speed
    
    def drive(self):
        print(Fore.GREEN + f"Driving at maximum speed of {self.max_speed}")


# Реалізуйте клас Car, який наслідує функціонал від Engine і Vehicle:
# Додайте атрибут model для зберігання назви моделі машини.
# Перевизначте метод drive() так, щоб він виводив повідомлення "Car {model} is driving at {max_speed}".

class Car(Vehicle):
    '''
    3. Реалізуйте клас Car, який наслідує функціонал від Engine і Vehicle:
    Додайте атрибут model для зберігання назви моделі машини.
    Перевизначте метод drive() так, щоб він виводив повідомлення "Car {model} is driving at {max_speed}".

        Engine
    |
    |
    Vehicile  
           |
           |
           Car
    '''
    def __init__(self, max_speed: float, model: str):
        Vehicle.__init__(self, max_speed)
        self.model = model
    
    def drive(self):
        print(Fore.YELLOW + f"Car {self.model} is driving at {self.max_speed}")

# Реалізуйте клас Boat, який також наслідує Engine і Vehicle:
# Додайте атрибут type для зберігання типу човна (наприклад, моторний, вітрильний).
# Перевизначте метод drive() так, щоб він виводив повідомлення "Boat of type {type} is sailing at {max_speed}".

class Boat(Vehicle):
    '''
    4. Реалізуйте клас Boat, який також наслідує Engine і Vehicle:
    Додайте атрибут type для зберігання типу човна (наприклад, моторний, вітрильний).
    Перевизначте метод drive() так, щоб він виводив повідомлення "Boat of type {type} is sailing at {max_speed}".

    Engine
    |
    |
    Vehicile  
    |       |
    |       |
    car     Boat
    '''
    def __init__(self, max_speed: float, type: str):
        Vehicle.__init__(self, max_speed)
        self.type = type
    
    def drive(self):
        print(Fore.GREEN + f"Boat of type {self.type} is sailing at {self.max_speed}")

# Створіть клас AmphibiousVehicle, який наслідує Car і Boat:
# Метод drive() повинен перевіряти, якщо транспортний засіб знаходиться на суші — виводити повідомлення для машини, а якщо на воді — для човна.
# Використовуйте атрибут is_on_land для визначення поточного стану.

class AmphibiousVehicle(Car, Boat):
    '''
    5. Створіть клас AmphibiousVehicle, який наслідує Car і Boat:
    Метод drive() повинен перевіряти, якщо транспортний засіб знаходиться на суші — виводити повідомлення для машини, а якщо на воді — для човна.
    Використовуйте атрибут is_on_land для визначення поточного стану.

    Engine
    |
    |
    Vehicile  
    |       |
    |       |
    car     Boat
        \\/      
  AmphibiousVehicle
    '''
    def __init__(self, Car_item: Car, Boat_item: Boat, is_on_land: bool):
        Car.__init__(self, Car_item.max_speed, Car_item.model)
        Boat.__init__(self, Boat_item.max_speed, Boat_item.type)
        self.is_on_land = is_on_land

    def drive(self):
        #i used explicion call to class bc of the diamond problem, if i call drive() its will call it from Car bc its first in mro
        if self.is_on_land:
            Car.drive(self) #Car {model} is driving at {max_speed}
        else:
            Boat.drive(self) #Boat of type {type} is sailing at {max_speed}

'''
------------------------------task2----------------------------------
'''
# 2. Створіть клас Library, який буде представляти бібліотеку. Бібліотека повинна містити список книг. Для роботи з об’єктами цього класу реалізуйте перевантаження операторів.

#    Для книги також створіть клас, перевантажте рядкове представлення (str). Для книги реалізуйте оператори порівняння за кількістю сторінок.
#    Реалізуйте property для полів книги.

# У бібліотеці необхідно реалізувати такі методи:
# - додавання книги в бібліотеку — має бути метод і оператор +=, який додає книгу
# - видалення книги — метод і оператор -=
# - перевірка, чи міститься книга в бібліотеці — оператор in
# - перевантажити len, який буде повертати кількість книг у бібліотеці

class Book:
    '''
    Для книги також створіть клас, перевантажте рядкове представлення (str).
    Для книги реалізуйте оператори порівняння за кількістю сторінок.
    Реалізуйте property для полів книги.

    '''
    def __init__(self, title: str, author: str, pages: int):
        self.__title = title
        self.__author = author
        self.__pages = pages

    '''Properties'''        
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def pages(self):
        return self.__pages
    
    '''magic methods'''
    '''equality operator bc of contain its check book by title and author, and not by pages'''
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__title == other.__title and self.__author == other.__author
    
    '''comparison operators'''
    def __lt__(self, other):
        return self.__pages < other.__pages

    def __gt__(self, other):
        return self.__pages > other.__pages

    def __ge__(self, other):
        return self.__pages >= other.__pages
    
    def __le__(self, other):
        return self.__pages <= other.__pages

    def __str__(self):
        return f"'{self.__title}' by {self.__author}, {self.__pages} pages"

class Library:
    '''
    Створіть клас Library, який буде представляти бібліотеку. Бібліотека повинна містити список книг. Для роботи з об’єктами цього класу реалізуйте перевантаження операторів.

    to do:  
        У бібліотеці необхідно реалізувати такі методи:
        - додавання книги в бібліотеку — має бути метод і оператор +=, який додає книгу
        - видалення книги — метод і оператор -=
        - перевірка, чи міститься книга в бібліотеці — оператор in
        - перевантажити len, який буде повертати кількість книг у бібліотеці
    '''
    def __init__(self):
        self.books = []
    
    '''Methods'''
    def add_book(self, book: Book):
        self.books.append(book)
    def remove_book(self, book: Book):
        self.books.remove(book)

    '''operators override'''
    def __iadd__(self, book: Book):
        self.add_book(book)
        return self

    def __isub__(self, other):
        self.remove_book(other)
        return self

    def __contains__(self, item):
        return item in self.books
    
    def __len__(self):
        return len(self.books)
    
    def __str__(self):
        return f"Library with {len(self)} books: "+"\n" + ",\n".join(str(book) for book in self.books)


'''
-------------------------------task3----------------------------------
'''
# 3. Напишіть клас-декоратор, який кешує результати методів класу, використовуючи аргументи методу як ключ для кешу. Якщо метод викликається з тими ж аргументами — повертайте вже обчислений результат із кешу.
# Якщо ні — обчислюйте та зберігайте результат у кеші.

class cache_deco:
    '''
    Напишіть клас-декоратор, який кешує результати методів класу, використовуючи аргументи методу як ключ для кешу. 
        - Якщо метод викликається з тими ж аргументами — повертайте вже обчислений результат із кешу.
        - Якщо ні — обчислюйте та зберігайте результат у кеші.
    '''
    def __init__(self, orig_func):
        self.orig_func = orig_func
        self.cache = {}
        update_wrapper(self, orig_func)
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Привязка к экземпляру класса 
        return MethodType(self, instance)
    
    def __call__(self, *args, **kwargs):
        cache_key = (args, frozenset(kwargs.items()))
        
        # Если результат уже есть в кэше, просто возвращаем его
        if cache_key in self.cache:
            print(f"{Fore.LIGHTBLACK_EX}Returning cached result for arguments: {cache_key} - {self.cache[cache_key]}")
            return self.cache[cache_key]
            
        # Если результата нет, вычисляем, сохраняем в кэш и возвращаем
        result = self.orig_func(*args, **kwargs)
        self.cache[cache_key] = result
        return result
    
  

'''
-------------------------------demonstration----------------------------------
'''

if __name__ == "__main__":
    
    @TryCatch
    def task1():
        line("Task 1 - Engine and Vehicle classes")
        line("different colors to show from which class the method is called")

        car = Car(500, "Honda")#model
        boat = Boat(50, "This sailind one person thing wroom")#type

        amphibious_vehicle = AmphibiousVehicle(car, boat, True)
        amphibious_vehicle.start_engine() #Engine started
        amphibious_vehicle.drive() #Car Honda is driving at 200
        amphibious_vehicle.is_on_land = False
        amphibious_vehicle.drive() #Boat of type This sailind one person thing wroom is sailing at 50
        amphibious_vehicle.stop_engine() #Engine stopped

        line("Technical part", Fore.LIGHTBLACK_EX)
        print(Fore.LIGHTBLACK_EX + str(amphibious_vehicle.__dict__))
        print(Fore.LIGHTBLACK_EX + str(amphibious_vehicle.__class__.__mro__))


    @TryCatch
    def task2():
        line("Task 2 - Library and Book classes")
        line("Book operations")
        book1 = Book("Methodius Buslaev. The Dryad's Necklace", "Dmitry Yemets", 384)
        book2 = Book("Azazel", "Boris Akunin", 250)
        book3 = Book("Im tired, boss", "Sertan Someone", 250)
        
        line("String representation", Fore.MAGENTA)

        print(book1) #'Methodius Buslaev. The Dryad's Necklace' by Dmitry Yemets, 384 pages

        line("Comparison operators", Fore.MAGENTA)
        yes_no = lambda condition: f"{Fore.GREEN}Yes" if condition else f"{Fore.RED}No"

        question = lambda book1, book2: f"Is '{book1.title}' longer than '{book2.title}'? {yes_no(book1 > book2)}"
        print(question(book1, book2)) #yes
        print(question(book2, book3)) #no
        
        question = lambda book1, book2: f"Is '{book1.title}' shorter or equal than '{book2.title}'? {yes_no(book1 <= book2)}"
        print(question(book1, book2)) #no
        print(question(book2, book3)) #yes

        line("Properties", Fore.MAGENTA)
        compareBook = Book("Azazel", "Boris Akunin", 400)
        question = lambda book1, book2: f"Is '{book1.title}' are the same book as '{book2.title}'? {yes_no(book1 == book2)}"
        print(question(book1, book2)) #no
        print(question(book2, compareBook)) #yes




        line("Library operations")
        library = Library()

        line("Add", Fore.MAGENTA)
        library += book1
        library.add_book(book2)
        library += book3
        print(library)

        line("Remove", Fore.MAGENTA)
        library -= book2
        library.remove_book(book3)
        print(library)

        line("Contain", Fore.MAGENTA)
        question = lambda book: f"Is {book.title} in library? {yes_no(book in library)}"

        print(question(book1))
        print(question(book3))

        line("Length", Fore.MAGENTA)
        print(f"Number of books in library: {len(library)}")


    from time import sleep, perf_counter
    from random import randint 

    class sample_class:
        @cache_deco
        def sample_method(self, x, sleep_time = 1):
            sleep(sleep_time)  
            return x * x



    def task3():
        line("Task 3 - Caching class decorator")
        obj = sample_class()
        l = [5,5,5,6,6,3,5]

        start_time1 = perf_counter()
        for i in l:
            start_time = perf_counter()
            print(f"{Fore.BLUE}Result for {i}: {obj.sample_method(i, sleep_time=5)}")
            end_time = perf_counter()
            print(f"{Fore.LIGHTBLACK_EX}Time taken for {i}: {end_time - start_time:.2f} seconds")
            line(color=Fore.LIGHTMAGENTA_EX)



        end_time1 = perf_counter()
        print(f"{Fore.LIGHTMAGENTA_EX}Total time taken:{end_time1 - start_time1:.2f} seconds")
########################Run#####################
    # task1()
    # task2()
    task3()


