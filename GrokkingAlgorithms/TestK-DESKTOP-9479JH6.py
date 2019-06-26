def sum2(a, b):
    if not a.isdigit() and not b.isdigit():
        return "all arguments are not a numbers"
    if not a.isdigit():
        return "1st argument is not a number"
    if not b.isdigit():
        return "2nd argument is not a number"
    else:
        return int(a) * int(b)

print(sum2('4','dgfg'))