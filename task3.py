#function
import math


def factorial_rec(n):
    if n == 0:
        return 1
    else :
        return n * factorial_rec(n - 1)
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial_rec(num)}")


#module
num = int(input("Enter a number: "))
def sqare(num):
    num * num
    return num ** 2
print(f"Square of {num} is {sqare(num)}")


output = math.log(num)
print(f"log of {num} is {output}")
output = math.sqrt(num)
print(f"squareroot of {num} is int{output}")
output = math.radians(num)
print(f"radians of {num} is {output}")




