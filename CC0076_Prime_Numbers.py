primes = [2, 3]
n = int(input("Please, enter a number: "))
for i in range(2, n+1):
    if i%2!= 0 and i%3!= 0:
        primes.append(i)
print(primes)