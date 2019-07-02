#==================================================================================
#Statement of the problem
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
#===================================================================================

#import modules

import numpy as np 

# define function
# 1 liner (This is faster)
def maxpalindrome(start,end):
    """
    This function checks whether the number is palindrome or not  

    Arguments:
        start -- (int) 1st element of the range 
        end   -- (int) last element of the range 
    
    Returns:
        val -- maximum palindrome value and its corresponding factors
    """
    val = max([(x * y, x, y) for x in range(start, end+1) for y in range(start, end+1) if palindrome(x * y) == True])
    return val






# note this method eates up a lot of memory. Not efficient for this problem. This might be usefull for some other case.

def palindrome(number):
    """
    This function checks whether the number is palindrome or not 

    Arguments:
        number -- (int) check whether the number is palindrome or not 
    
    
    Returns:
        True -- if True
        False -- if False
    """
    number = str(number)
    if ( list(number) == list(reversed(number))):
        return True
    else:
        return False

def max_palindrome(start,end):
    """
    This function checks whether the number is palindrome or not  

    Arguments:
        start -- (int) 1st element of the range 
        end   -- (int) last element of the range 
    
    Returns:
        mat -- maximum palindrome value and its corresponding factors
    """
    #vectorize the function for faster processing.
    ispalindrome = np.vectorize(palindrome)
    mat = np.arange(start,end)
    mat = np.outer(mat,mat)
    #b = np.tril(b)  This is optional. trail replaces above/below diagonal values of a
    #symmetric matrix to 0
    #b[b == 0] = 12
    mat = np.max((ispalindrome(mat)==True)*mat)
    return mat



if __name__ == "__main__":
    print (maxpalindrome(start = 100,end = 999)[0])
    #print (max_palindrome(start = 100,end = 999)) #not recommended
