#==================================================================================
#Statement of the problem
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
#===================================================================================


'''
There are several ways to do this problem, The least memory consuming is

'''


#import modules

import numpy as np

# define function
def ismaxprime(val):
    """
    This function return the maximum prime number for a given array 

    Arguments:
        val -- (int) the number whose max prime factor is to be found 
    
    
    Returns:
        val -- the maximum prime number
    """
    
    #If a number is divisible between any number between 2 and the number,
    #it's not a prime number
    arr = factor(val).reshape(-1,1) 
    for value in reversed(arr):
        if (isprime(value) == True ):
            return int(value)
        else:
            continue
    else:
        print ("No prime facotor present")

#check for prime number
def isprime(num):
    """
    This function checks for prime numbers 

    Arguments:
        num -- (int) the number to check 
    
    
    Returns:
        val -- True if prime, False for not prime
    """
    
    #If a number is divisible between any number between 2 and the number-1,
    #it's not a prime number

    assert num >= 2
    if (min(num % np.arange(2,np.sqrt(num)+1)) == 0):
        return False
    else:
        return True
    
def factor(num):
    """
    This function will generate all the foctors for a given number 

    Arguments:
        num -- (integer) the number for which we need the factors
    
    
    Returns:
        out -- a list of numbers which are foctors of the input number
    """
    divide = np.arange(2,(np.sqrt(num)+1))
    out = num % divide
    return np.take(divide,np.where(out==0),axis = 0)

if __name__ == "__main__":
    print (ismaxprime(600851475143))
    
    
    

 
 
