with open('dataset_3363_4.txt', 'r', encoding='utf-8') as a:
     strings = a.read().splitlines()
lengString = len(strings)
rmath, rhys, rukr = 0, 0, 0
with open('dataset_3363_4.txt', 'w') as b:
    for s in strings:
        for i in range(1):
            name, math, phys, ukr = s.split(';')
            res = (int(math) + int(phys) + int(ukr))/3
            b.write(str(res) + '\n')
            rmath += int(math)
            rhys += int(phys)
            rukr += int(ukr)
    b.write(str(rmath / lengString) + ' ' + str(rhys / lengString) + ' ' + str(rukr / lengString) + '\n')
