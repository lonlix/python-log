# def parent():
#     print("Printing from parent()")
#
#     def first_child():
#         print("Printing from first_child()")        #Внутренние функции вау просто идеально понял
#
#     def second_child():
#         print("Printing from second_child()")
#
#     second_child()
#     first_child()
# parent()
# def parent(num):
#     def first_child():
#         return "Hi, I'm Elias"
#
#     def second_child():
#         return "Call me Ester"  ссылки фунцкий прокольно тож понял
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# first = parent(1)
# second = parent(2)
# first()

# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper    уже декоратор который обернул функцию круто очень хах
#
#
# def say_whee():
#     print("Whee!")
#
# say_whee = decorator(say_whee)
# say_whee()
from datetime import datetime

def not_night(func):
    def wrapper():
        if 7 < datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper

@not_night
def say_whee():
    print("Whee!")

say_whee()