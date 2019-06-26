for a in range(1, 11):
    for b in range(1, 11):
        #if a*b == 90:
            #print(str(a * b), end="")
            #continue
        if a*b > 9:
            print(str(a * b), end="  ")
        else:
            print(str(a * b), end="   ")
    print("\n")

# for a in range(1, 11):
    # for b in range(1, 11):
         # print(str(a * b), end=" " if a*b >=10 else (str((a*b), end='  '))