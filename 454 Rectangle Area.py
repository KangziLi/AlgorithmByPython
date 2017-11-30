# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:49:55 2017

@author: KangziLi
@source: lintcode - 454. Rectangle Area
"""

class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    def getArea(self):
        return self.width * self.height