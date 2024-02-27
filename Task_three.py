# Создайте функцию генератор чисел Фибоначчи
def fibonacci_gen(n):
    num = 1
    num1 = 0
    num2 = 1
    for i in range(n):
        yield num
        num = num1 + num2
        num1 = num2
        num2 = num


for i in fibonacci_gen(10):
    print(i)
