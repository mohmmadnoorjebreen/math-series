
# create function that take number and retune the fibonacci series for it

def fibonacci(n):
   if n < 0:
       return 'invalid value'
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
   
 
# create function that take number and retune the lucas number for it
   
def lucas(n):
    if n<0:
        return 'invalid value'
    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1) + lucas(n-2)

# Combine the two function in general function

def sum_series(n,def1=0,def2=1):
    if n==0:
        return def1
    if n==1:
        return def2
    return sum_series(n-1,def1,def2) + sum_series(n-2,def1,def2)
       
    





