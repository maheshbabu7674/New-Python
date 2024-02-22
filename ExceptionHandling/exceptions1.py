def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
try:
    num=1
    enterage(num)
except ValueError:
    print("only positive integers are allowed")
except:
    print("something is wrong")

    # output:
    #age is odd

try:
    number=one
    print("the number is ",number)
except NameError as x:
    print("Exception:", x)