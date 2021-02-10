
def cm_miles():
    cm = float(input("Enter CM Distance: "))
    miles = cm / 160934.4
    print("Miles: {}".format(miles))

def cm_km():
    cm = float(input("Enter CM Distance: "))
    km = cm / 100000
    print("KM: {}".format(km))

def km_miles():
    km = float(input("Enter KM Distance : "))
    miles = km * 0.6214
    print("Miles: {}".format(miles))

def miles_km():
    miles = float(input("Enter miles Distance: "))
    km = miles * 1.609344
    print("KM: {}".format(km))

def miles_cm():
    miles = float(input("Enter miles Distance: "))
    cm = miles * 160934.4
    print("CM: {}".format(cm))

def KM_CM():
    km = float(input("Enter KM Distance: "))
    cm = km * 100000
    print("CM: {}".format(cm))

def print_menu():
    print('1. Miles to KM')
    print('2. Miles to CM')
    print('3. KM to Miles')
    print('4. KM to CM')
    print('5. CM to KM')
    print('6. CM to Miles')

    choise = input(str("Choice Conversion: "))

    if choise == '1':
        miles_km()
    elif choise == '2' :
        miles_cm()
    elif choise == '3':
        km_miles()
    elif choise == '4':
        KM_CM()
    elif choise == '5':
        cm_km()
    elif choise == '6':
        cm_miles()

print_menu()



