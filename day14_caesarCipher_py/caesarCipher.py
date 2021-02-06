import collections
import string

def caesar(rotate, number_rotate):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_rotate)
    lower.rotate(number_rotate)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))


    

print (caesar("sghr hr sn dzrx", 0))