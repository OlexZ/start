a = b = 5

n = int(input("Кількість ітерацій_"))

while n > 0:
    a, b = b, a + b
    n-=1
    print(a, end=" ")