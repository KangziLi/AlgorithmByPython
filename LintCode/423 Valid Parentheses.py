# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:03:52 2017

@author: KangziLi
@source: lintcode - 423. Valid Parentheses
"""

class Solution:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    @param: s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        stack = []
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ']' and stack[-1] != '[' or c == ')' and stack[-1] != '(' or c == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack