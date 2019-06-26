text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
words = ['i', 'was', 'three', 'near']
text = text.lower()
bigText = text.split()
res = {}
for i in words:
    res[i] = bigText.count(i)
print(res)

#BestSolution
#def popular_words(text, words):
#lower_count = text.lower().split().count
#    return {word: lower_count(word) for word in words}
