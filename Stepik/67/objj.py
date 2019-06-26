objects = [1, 2, 1,  set()]
objecto = []
for obj in objects: # доступная переменная objects
    if obj not in objecto:
        objecto.append(obj)


print(len(objecto))