prime = list(range(2,100))
i = 0
while i < len(prime) - 1:
    j = i + 1
    while j < len(prime):
        if prime[j] % prime[i] == 0:
            del prime[j]
        else:
            j += 1
    i += 1
print (prime)

    
