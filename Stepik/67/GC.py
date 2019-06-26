st = input().lower()
b = st.count('g')
b += st.count('c')
print(float(b / len(st))*100)