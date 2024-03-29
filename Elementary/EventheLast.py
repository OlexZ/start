def checkio(array):
    num = 0
    if not array:
        return num

    for i in array[::2]:
        num += int(i)
    num *= array[-1]
    return num


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#   BEST SOLUTION
#   def checkio(array):
#       """
#            sums even-indexes elements and multiply at the last
#        """
#        if len(array) == 0: return 0
#       return sum(array[0::2]) * array[-1]
#
#
#   # These "asserts" using only for self-checking and not necessary for auto-testing
#    if __name__ == '__main__':
#        assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#        assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#        assert checkio([6]) == 36, "(6)*6=36"
#        assert checkio([]) == 0, "Empty"
