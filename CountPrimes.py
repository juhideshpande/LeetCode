class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        count = 0
        primes = [True for i in range(n+1)]
        primes[0],primes[1]=False, False
        for i in range(2,n):
            if primes[i] == True:
                count+=1
                j = 2
                while j*i<n:
                    primes[j*i] = False
                    j+=1
        return count
