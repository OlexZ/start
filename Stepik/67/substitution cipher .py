source_alphabet, end_alphabet, encrypt, decipher = [input() for i in range(4)]  #   'abcd', '*d%#', 'abacabadaba', '#*%*d*%'
cipher = {}
source_alphabet += end_alphabet
res_encrypt, res_decipher = '', ''
for i in range(int(len(source_alphabet) / 2)):
    cipher.setdefault(source_alphabet[i], source_alphabet[i + int(len(source_alphabet) / 2)])

for cip in range(len(encrypt)):
    for key, value in cipher.items():
        if encrypt[cip] == key:
           res_encrypt += value

for cip in range(len(decipher)):
    for key, value in cipher.items():
        if decipher[cip] == value:
            res_decipher += key

print(res_encrypt)
print(res_decipher)


# start = input()
# fin = input()
# forSh = input()
# forDesh = input()
#
# resSh = ''
# resDesh = ''
#
# for ch in forSh :
#     resSh += fin[ start.find(ch) ]
#
# for ch in forDesh :
#     resDesh += start[ fin.find(ch) ]
#
# print(resSh)
# print(resDesh)