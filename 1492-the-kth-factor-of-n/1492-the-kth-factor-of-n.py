class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = [], int(n**0.5)
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x
        
        # If n is a perfect square
        # we have to skip the duplicate 
        # in the divisor list
        if (sqrt_n * sqrt_n == n):
            k += 1
                
        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1