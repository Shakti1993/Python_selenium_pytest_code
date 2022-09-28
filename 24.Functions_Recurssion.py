## This is how we import any function from different file into another file..
# import Functions

# Functions.add(15,23)

# driver = Functions

# print(driver)

###----------------------------------------------------

##Functions_Recurrsion---

#1. How to find Factorial of any number..

counter = int(input("Write any number to find the factorial: "))

result = 1

while (counter > 1):
    result *= counter
    counter-=1
print("Factorial of given number:", result)


# def getFunction():
#     print(int(input("write something: ")))

# getFunction()

## Function Recursion


def get_facorial(number : int):
    if number == 1 or number == 0:
        return 1
    return number * get_facorial(number - 1)

Fact = get_facorial(5)

print("Factorial of given number: ", Fact)

