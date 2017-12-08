for i in range(2, 101):
    k = int(i ** 0.5)
    isprime = True
    for j in range(2,k+1):
        if i % j==0:
            isprime = False
            break
    if(isprime):
        print(i, ' ') #i is prime
