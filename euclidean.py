def first():
    mas = returnTwoNumbers()
    a=mas[0]
    b=mas[1]
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)

def second():
    mas = returnTwoNumbers()

def returnTwoNumbers():
    print('Введите 2 числа')
    firstNum=int(input())
    secondNum=int(input())
    return [firstNum, secondNum]

print('Обычный евклид (1) или расширенный? (2)')
choice = int(input())

if choice == 1:
    first()
elif choice == 2 :
    second()
else:
    print('ок поняла')
