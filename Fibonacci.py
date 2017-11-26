class Solution:
    '''
    Find the Nth number in Fibonacci sequence.
    A Fibonacci sequence is defined as follow:
        The first two numbers are 0 and 1.
        The i th number is the sum of i-1 th number and i-2 th number.
    The first ten numbers in Fibonacci sequence is:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
    # @param n: an integer
    # @return an integer f(n)
    '''
    def fibonacci(self,n):
        a=0
        b=1
        if n<=2:
            return n-1
        else:
            for i in range(2,n):
                c=a+b
                a=b
                b=c
            return c
