import time

print (" 1.Timer for second")
print (" 2.timer for minutes")
print (" 3.timer for hour")


def second():
    seconds = int(input("How many Second To wait: "))
    for i in range(seconds):
        print(str(seconds - i) + " Seconds Remain")
        time.sleep(1)

def minutes():
    minut = int(input("How many Minutes To Wait: "))
    for i in range(minut):
        print(str(minut - i) + " Minutes Remain" )
        time.sleep(60)
        

def hour():
    hours = int(input("How many Hour To wait: "))
    for i in range(hours):
        print(str(hours - i) + " Hours Remain")
        time.sleep(3600)

def enter_input():
    user_input = int(input("What Timer you need? : "))

    if user_input == 1:
        second()
       
    elif user_input == 2:
        minutes()
    elif user_input == 3:
        hour()
        
enter_input()

