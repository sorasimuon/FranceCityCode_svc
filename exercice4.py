# Python program to count 
# ways to reach nth stair 
  
# Recursive function to find  
# Nth fibonacci number 
def fib(n): 
    if n <= 1: 
        return n 
    return fib(n-1) + fib(n-2) 
  
# Returns no. of ways to  
# reach sth stair 
def countWays(s): 
    return fib(s + 1) 
  
# Driver program 
s = 5
print ("Number of ways = ") 
print(countWays(s))



# A program to count the number of ways 
# to reach n'th stair 
  
# Recursive function used by countWays 
def countWaysUtil(n, m): 
    if n <= 1: 
        return n 
    res = 0
    i = 1
    while i<= m and i<= n: 
        res = res + countWaysUtil(n-i, m) 
        i = i + 1
    return res 
      
# Returns number of ways to reach s'th stair     
def countWays(s, m): 
    return countWaysUtil(s + 1, m) 
      
  
# Driver program 
s, m = 4, 2
print ("Number of ways =", countWays(s, m)) 
  
# Contributed by Harshit Agrawal 