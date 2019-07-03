#==================================================================================
#Statement of the problem
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
#=================================================================================== 


# Recursive function to return gcd of a and b 
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 


def EvenlyDivisible(start , end):
    res = 1
    for i in range(start,end+1):
        res *= i//gcd(i,res)
        print (res)
    return res

print (EvenlyDivisible(1,20))

  
