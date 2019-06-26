# https://stepic.org/media/attachments/course67/3.6.2/672.txt
import requests
surl = 'dataset_3378_2.txt'
with open(surl, 'r') as urlAdres:
    url = urlAdres.readline().strip()
    r = requests.get(url)
    temp = r.text.strip()

with open(surl, 'w') as urlAdres:
    urlAdres.write(temp + '\n')
    num_lines = sum(1 for line in open('dataset_3378_2.txt'))

# import requests
#
# print(requests.get(open('in.txt').readline().strip()).text.count('\n'))

