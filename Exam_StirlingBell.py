###For some reason it doesn't give me the same results for large n and k such as 20
###and 15 as in the examples shown as tests

#Definition of the stirling number according to wikipedia
def stirling_number(n,k):
    sum = 0
    for i in range(0,k+1):
        sum = sum+((-1)**(k-i))*(math.factorial(k)/(math.factorial(k-i)*math.factorial(i))
        )*(i**n)
    result = (1./math.factorial(k))*sum
    return int(result)
    
#Definition of the stirling number according to wolfram math
def stirling_number_wolf(n,k):
    sum = 0
    for i in range(0,k+1):
        sum = sum+((-1)**i)*(math.factorial(k)/(math.factorial(k-i)*math.factorial(i)))*(
        (k-i)**n)
    result = (1./math.factorial(k))*sum
    return int(result)
    
def bell(n):
    result = 0
    for k in range(1,n+1):
        result = result+stirling_number(n,k)
    return result