class Solution:
    def countPrimes(self, n):
        def prime(number):
            for num in range(2, math.floor(sqrt(number))+1):
                if number%num == 0:
                    return False
            return True
        counter = 0
        for i in range(2, n):
            if prime(i):
                counter += 1
        return counter

class Solution1:
    def countPrimes(self, n):
        #Sieve of Eratosthenes
        def prime(number):
            for num in range(2, math.floor(sqrt(number))+1):
                if number%num == 0:
                    return False
            return True
        marked = [True for i in range(n)]
        if n < 2:
            return 0
        marked[0] = marked[1] = False
        
        for i in range(2, n):
            if marked[i] == True:
                if prime(i):
                    times = 2
                    current = i*times
                    while current < n:
                        marked[current] = False
                        times += 1
                        current = i*times
        return sum(1 for i in marked if i == True)

class Solution1:
    def countPrimes(self, n):
        #Sieve of Eratosthenes
        #improved version
        def prime(number):
            for num in range(2, math.floor(sqrt(number))+1):
                if number%num == 0:
                    return False
            return True
        marked = [True for i in range(n)]
        if n < 2:
            return 0
        marked[0] = marked[1] = False
        
        for i in range(2, math.floor(sqrt(n))): #doesnt need to go all the way to n. just like what's in the function prime. a number that's not prime will be covered already in line 57 to 60.
            if marked[i] == True:
                if prime(i):
                    times = 2
                    current = i*times
                    while current < n:
                        marked[current] = False
                        times += 1
                        current = i*times
        return sum(1 for i in marked if i == True)
                

