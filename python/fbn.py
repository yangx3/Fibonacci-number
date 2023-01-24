#Fibonacci Number python
#Author: Danny
#Description
#This is a code example for Fibonacci number. Using recursion.
#This is not the best solution. Keep in mind FN is start with 0, and it is the 0th number.


#Calculate the nth number of Fibonacci number
def Fibonacci_recirsion(n):
    #checking if passing value is number
    if(type(n) != int):
        return -1
    #checking if passing value is valid number
    if n <= 0:
        return 0
    #return number for the first and second number of FN
    if n < 3:
        return 1
    #Making a recursion
    else:
        return Fibonacci_recirsion(n-1) + Fibonacci_recirsion(n-2)

def Fibonacci_forward(n):
    #checking if passing value is number
    if(type(n) != int):
        return -1
    #checking if passing value is valid number
    if n <= 0:
        return 0
    if n < 3:
        return 1
    #create first and second number
    f1 = 1
    f2 = 1
    fn = 0
    #in the loop, n will always greater than 2.
    for i in range(2, n):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn
