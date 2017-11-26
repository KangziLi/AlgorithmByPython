"""
Created on Sun Nov 26 18:35:06 2017

@author: KangziLi
@source: lintcode - 212. Space Replacement
"""

class Solution:
    """
    Write a method to replace all spaces in a string with %20. The string is given in a characters array, you can assume it has enough space for replacement and you are given the true length of the string.
    You code should also return the new length of the string after replacement.
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        if length == 0 or string == None:
            return length
        space = 0
        for i in string:
            if i == ' ':
                space += 1
        reallen = length + space * 2
        index = reallen - 1
        for i in range(length-1, -1, -1):
            if string[i] == ' ':
                string[index] = '0'
                string[index - 1] = '2' 
                string[index - 2] = '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1 
        return reallen