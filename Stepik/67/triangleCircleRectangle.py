name = str(input())

if name == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif name == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a*b)
elif name == "круг":
    a = float(input())
    s = 3.14*(a**2)
    s = float('{:.1f}'.format(s))
    print(s)
