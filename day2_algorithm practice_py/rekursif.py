

def ulang(a, b):
    if a >= b:
        exit()
    else:
        print(a)
        return ulang(a + 2, b)

ulang(1, 100)
