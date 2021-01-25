

def primer():
    i = 2
    while i < 200:
        j = 2
        while(j <= (i/j)):
            if not (i%j):
                break
            j += 1
        if (j > i/j): print(i,"bilangan prima")
        i += 1

primer()