"""
Created on Sun Nov 26 18:35:06 2017

@author: KangziLi
@source: lintcode - 204. Singleton
"""

class Solution:
	'''
	Singleton is a most widely used design pattern. If a class has and only has one instance at every moment, we call this design as singleton. For example, for class Mouse (not a animal mouse), we should design it in singleton.
	You job is to implement a getInstance method for given class, return the same instance of this class every time you call this method.
    # @return: The same instance of this class every time
    '''
    @classmethod
    def getInstance(cls):
        return cls