age = 16
name = "Glib"
height = 175.4
student = True
grades = [5, 5, 4, 4]
coordinates = (50.46, 30.42)
numbers = {1, 2, 3}
person = {"name": "Glib", "age": 16}
print("age,", type(name).__name__, ":", name)
print("height,", type(height).__name__, ":", height)
print("student,", type(student).__name__, ":", student)
print("grades,", type(grades).__name__, ":", grades)
print("numbers,", type(numbers).__name__, ":", numbers)
print("coordinates,", type(coordinates).__name__, ":", coordinates)
print("person,", type(person).__name__, ":", person)

first_n = 10
second_n = 4

a = first_n + second_n # додає числа
b = first_n - second_n # віднімає числа
c = first_n * second_n # множить числа
d = first_n / second_n # ділить числа
e = first_n % second_n # показує остачу від ділення
f = first_n ** second_n # підносить перше число до степеня другого
g = first_n // second_n # бере тільки цілу частину від ділення
print(a, b, c, d, e, f, g)