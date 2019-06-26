lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'thw',
    'two': 'two',
    'three': 'three'
}
string = 'hello world'

iterator = iter(book)
while True:
    try:
        i = next(iterator)
        print(i)
    except StopIteration:
        break
