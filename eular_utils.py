import numpy as np


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
    if (num <= 3):
        return True
    elif (min(num % np.arange(2,np.sqrt(num)+1)) == 0):
        return False
    else:
        return True
 
def factor(num):
    """
    This function will generate all the prime foctors for a given number 

    Arguments:
        num -- (integer) the number for which we need the factors
    
    
    Returns:
        out -- a list of prime numbers which are foctors of the input number
    """
    prime = []
    if (isprime(num) == True):
        prime.append(num)
        return prime   #return "prime.append" won't work here we will be assigning an output to the act of appending which has no output
    else:    
        divide = np.arange(2,(np.sqrt(num)+1))
        out = num % divide
        out = np.take(divide,np.where(out==0)[0],axis = 0)
        for value in reversed(out):
            if (isprime(value) == True ):
                prime.append(value)
            else:
                prime = prime
        return prime


