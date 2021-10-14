def first(mas):
    a=mas[0]
    b=mas[1]
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)

def second(mas):
    a=mas[0]
    b=mas[1]
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    print( x, y, a)


def returnTwoNumbers():
    print('Введите 2 числа')
    firstNum=int(input())
    secondNum=int(input())
    return [firstNum, secondNum]

print('Обычный евклид (1) или расширенный? (2)')
choice = int(input())

if choice == 1:
    first(returnTwoNumbers())
elif choice == 2 :
    second(returnTwoNumbers())
else:
    print('ок поняла')
