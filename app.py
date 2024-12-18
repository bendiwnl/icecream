"""
this is my first application
"""

from icecream import ic
from myhelp.helper import *


n1= input("please type number")
n2= input("please type number")
data=[3,5,6,7]

ar=[3,5,6,7,4,9,2,4]


#sum two numbers
def sum_two_numbers(n1,n2):
    return n1 + n2


def display():
    print(data)

    

# entry point for script execution
def main():
    print(f"the smaller number is: {smaller(n1,n2)}")
    print(f"the bigger number is:  {bigger(n1,n2)}")
    print(f"the sum is: {sum_two_numbers(n1,n2)}")
    display()




if __name__ == "__main__":
    main()
    ic(ar)