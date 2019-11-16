def isPrime(num):
    if num>1:
        for i in range(2, num):
            if(num%i)==0:
                break
        else:
                print(num, end=" ")
    

for i in range(1, 20):
    if isPrime(i+1):
                    print(i+1)
                    
print()
    
    
    
    
  