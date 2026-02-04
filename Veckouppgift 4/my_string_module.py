# My String module to take a string as a parameter


def string_parameter(name):
    print(f" {name} is a whiz at programming")
    return 0

def string_echo(name):
    print(f"{name}{name}")
    return 1

def checker_counter(counter):
    counter_final = 0
    while True:
            counter = input("Enter counter: ")
            if counter.isdigit() == True:
                counter_final = int(counter)
                break
            else:
                print("Invalid input! Enter a counter number. ")
    return counter_final

def echo_counter(name,counter):
    echo = ""
    if counter == 0:
        print("Zero counter")
    else:
        #counter = int(counter2)
        for i in range(counter):
            echo += name
    print(f"{echo}")
    return 2

def my_loop(i):
    y = 1
    for x in range(1,100):
        y *= 2
        if x == 5:
            print("End of loop.")
            break
        print(y)


