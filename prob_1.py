
#Statement of the problem
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

#import modules

import numpy as np

#create function

def sum_of_numbers(num=1000,divide1 = 3,divide2 = 5):
    """
    This function will calculate the sum of all the numbers divisible by divide.
    Default is 3

    Arguments:
        num -- an integer.A list will be created ranging from 1 to num (default is 1000).
        divide1 -- the number to check divisibility (default is 3).    
        divide2 -- the number to check divisibility (default is 5).    
    
    
    Returns:
        total -- sum of number divisible by divide.
    """
    total = sum([x for x in range(num) if (x % divide1 == 0 or x % divide2 == 0)])
    return total

if __name__ == "__main__":
    print (f'Sum is = {sum_of_numbers(num = 1000,divide1 = 3, divide2 = 5)}')

