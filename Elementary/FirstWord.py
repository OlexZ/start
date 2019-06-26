def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ')
    text = text.strip()
    txt = ''
    for i in text:
        if i is not ' ':
            txt += i
        else:
            break
    return txt
#BestSolution
#def first_word(text: str) -> str:
#    return re.search("([\w']+)", text).group(1)

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")