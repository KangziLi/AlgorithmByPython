class Solution:
    """
    Given number n. Print number from 1 to n. But:
        when number is divided by 3, print "fizz".
        when number is divided by 5, print "buzz".
        when number is divided by both 3 and 5, print "fizz buzz".
    @param n: An integer as description
    @return: A list of strings.
    For example, if n = 7, your code should return
        ["1", "2", "fizz", "4", "buzz", "fizz", "7"]
    """
    def fizzBuzz(self, n):
        return ['fizz'*(not i%3)+'buzz'*(not i%5) or str(i)for i in range(1,n+1)]
        '''
        results = []
        for i in range(1, n+1):
            if i % 15 == 0:
                results.append("fizz buzz")
            elif i % 5 == 0:
                results.append("buzz")
            elif i % 3 == 0:
                results.append("fizz")
            else:
                results.append(str(i))
        return results
        '''
        