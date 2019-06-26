# https://stepic.org/media/attachments/course67/3.6.3/699991.txt
import  requests
first = (open('dataset_3378_3.txt','r')).readline().strip()

temp = requests.get(first)
temp = temp.text
while True:
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + temp
    temp = requests.get(url)
    temp = temp.text.split()[0]
    if temp == 'We':
        print(temp)
        break
    print(temp)
res = requests.get(url).text.strip()
t = open('dataset_3378_3.txt', 'w')
t.write(res)
t.close()

print(res)