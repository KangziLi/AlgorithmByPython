"""
Created on Mon Nov 27 20:03:40 2017

@author: KangziLi
@source: lintcode - 56. Two Sum
"""

class Solution:
    """
    Given an array of integers, find two numbers such that they add up to a specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def valIndex(self, val, num):
        for i in range(len(num)):
            if num[i]==val:
                return i
        return -1
    
    def twoSum(self, numbers, target):
        length=len(numbers)
        for i in range(length):
            val = target - numbers[i]
            newlist = numbers[i+1:]
            k = self.valIndex(val,newlist)
            index = k+i+1
            if index != i:
                return [i+1,index+1]
        return [];