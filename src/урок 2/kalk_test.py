a = int(input("введите а "))
c = input("введите действие ")
b = int(input("введите b "))

if c == "+":
    print(a + b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "-":
    print(a - b)
elif c == "//":
    print(a // b)
elif c == "%":
    print(a % b)
else:
    print("введите правильное действие, лось  \n-,+,*,/,//,%")
