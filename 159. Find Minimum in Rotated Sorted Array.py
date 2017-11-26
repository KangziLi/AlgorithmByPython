"""
Created on Sun Nov 26 21:02:06 2017

@author: KangziLi
@source: lintcode - 159. Find Minimum in Rotated Sorted Array
"""

class Solution:
    """
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).Find the minimum element.
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        l = 0
        r = len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            m = int((l + r) / 2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]  