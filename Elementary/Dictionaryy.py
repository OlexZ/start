person = {}
s = 'Olexsandr Newman Kuiv MA 3 2 4 3 2 1'
s = s.split()
person['firstName'] = s[0]
person['secondName'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(person.values()  )
