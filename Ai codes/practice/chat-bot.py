def greet(name , year):
    print(f"Hello my name is {name}")
    print(f"i was made in year {year}")

def remind():
    print("please remind me your name")
    name = input()
    print(f"What a great name you have {name} !")


def guessAge():
    print("let me guess your age\n")
    print("give me the remainders of dividing your age by 3,5,7\n")

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age} years")


def count():
    print("let me prove to you that i can count till any number you enter\n")
    print("enter the number below\n")
    number = int(input())
    i=1
    while i != number+1:
        print(i,"\n")
        i = i+1
def test():
    print("lets test your programing knowledge !\n")
    print("select the correct option\n")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    ans = 2
    print("Enter your answer below\n")
    inp = int(input())

    while inp != ans:
        print("Ooops wrong anwer , try again!")
        inp = int(input())

    print("completed have a nice day")


def end():
    print("Thank you for conversing , bye bye")
    input()



greet("CCBOT", 2024)
remind()
guessAge()
count()
test()








