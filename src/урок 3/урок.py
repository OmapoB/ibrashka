counter = 0
print(f'счетчик до цикла {counter}')
while counter != 10:
    print(f'счетчик в цикле {counter}')
    counter += 10
else:
    print('конец')
"""
while условие:
    код
else:
    код
пока условие истино выполняется код
еlse выполняется при ложном условии
else не обязательно
"""
t = [1, 3, 4, 5, 2, 1]
for i in range(len(t)):
    print(f'i = {t[i]}')
