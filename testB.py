# py -m doctest  testB.py
# py -m doctest  testB.py -v
# import testB
# py -i testB.py
def bubu(a,b):
    '''

    bla bla
    :return:
    >>> bubu(2,2)
    4
    >>> bubu(2,3)
    6
    >>> bubu(2,5)
    10


    '''
    return a* b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
else:
    print(bubu(2,3))