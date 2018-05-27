#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:44:44 2018

@author: Kangzi Li

LeetCode: 690. Employee Importance
"""

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        table = {}
        for emp in employees:
            table[emp.id] = emp
        queue = [table[id]]
        ans = 0
        while queue:
            emp = queue.pop()
            for sub in emp.subordinates:
                queue.append(table[sub])
            ans += emp.importance
        return ans
                
        
        
