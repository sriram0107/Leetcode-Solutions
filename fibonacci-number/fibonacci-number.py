class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        
        f1 = 1
        f2 = 1
        f3 = 0
        for i in range(3,n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3
        