def mult(x, y):
    return x*y

print("Выберите операцию: 1-сложение, 2-вычитание, 3-умножение, 4-деление")
operation = input("Введите номер операции:")
n1 = int(input("Введите первое число:"))
n2 = int(input("Введите второе число:"))

if operation == '3':
    print(f"{n1} * {n2} = {mult(n1, n2)}")