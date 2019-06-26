a = ['a', 'bb', 'cCc']
b = ['c', 'bb', 'aaa']
for i in b:
    if i not in a:
        print(True)
    else:
        print(False)