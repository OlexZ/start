num = int(input())

res = num % 10
reshundred = num%100
if num >= 0 and num <= 1000:
    if reshundred >= 11 and reshundred <= 14:
        print(str(num) + " программистов")
    elif res == 1:
        print(str(num) + " программист")
    elif num == 0:
        print(str(num) + " программистов")
    elif res >= 2 and res <=4:
        print(str(num) + " программиста")
    elif (num >= 5 and num <= 1000):
        print(str(num) + " программистов")
else:
    print(str(num) + " Дохуя програмистов у нас столько нету")