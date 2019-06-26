a = float(input())
b = float(input())
module = input()

if (a == 0.0 or b == 0.0) and (module == "/" or module == "mod" or module == "div"):
    print("ти що геть клепки не маєш не діли на 0!")
else:
    if module == "mod":
        print(a % b)
    elif module == "pow":
        print(a ** b)
    elif module == "div":
        print(a // b)
    elif module == "*":
        print(a * b)
    elif module == "/":
        print(a / b)
    elif module == "-":
        print(a - b)
    elif module == "+":
        print(a + b)