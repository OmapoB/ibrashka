"""
ввод / вывод
print() выводит на экран то  что в скобках
"""
print("123")
"""
input() присваивает значение введенное с консоли
a = input("Подсказка") присваивает а значение вводимое
    с консоли и выводит на экран подсказку
    по умолчанию присваивает только строки 
"""
a = input("Введите а ")
"""
ветвление
if условие(boolean):
    код
выполняет код если условие истина
"""
if a == 1:
    print("a = ", a)
"""
if условие(boolean):
    код1
else:
    код2
    если условие истина то выполняется код1 если ложно то код 2
"""
if a == 1:
    print("a = ", a)
else:
    print("a != 1")
"""
if условие1(boolean):
    код1
elif условие2(boolean):
    код2
elif условие3(boolean):
    код3
else:
    код4
"""
if a == 1:
    print("a = ", a)
elif a == 2:
    print("a = ", a)
elif a == 3:
    print("a = ", a)
else:
    print("a != 1")
