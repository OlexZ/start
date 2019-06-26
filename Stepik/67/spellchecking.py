num_famous_words = int(input())
famous_words = []
line_of_text = []
temp = []
for i in range(num_famous_words):
    famous_words.append(input().lower())

num_line_of_text = int(input())

for i in range(num_line_of_text):
    line_of_text = input().lower().split()
    for q in line_of_text:
        if q not in famous_words and q not in temp:
            temp.append(q)
            print(q)

print(line_of_text)