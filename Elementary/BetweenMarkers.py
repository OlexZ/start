def between_markers(text: str, begin: str, end: str) -> str:
    beginMarker = text.find(begin) + len(begin)
    endMark = text.find(end)
    for i in text:
        if begin in text and end in text:
            return text[beginMarker:endMark]
        elif begin in text:
            return text[beginMarker:]
        elif end in text:
            return text[:endMark]
        elif begin not in text and end not in text:
            return text
        else:
            return ""
#BestSolution
#def between_markers(text: str, begin: str, end: str) -> str:
#    start = text.find(begin) + len(begin) if begin in text else None
#    stop = text.find(end) if end in text else None
#    return text[start:stop]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')