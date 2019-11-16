def isPrime(num):
    if num>1:
        for i in range(2, num):
            if(num%i)==0:
                print(num, "is not a prime number")
                break
        else:
                print(num,"is a prime number")
    

for i in range(1, 20):
    if isPrime(i+1):
                    print(i+1, end="")
                    
print()
    
    
    
    
  