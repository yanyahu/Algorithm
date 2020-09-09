#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            注意审题
            !!! It doesn't matter what values are set beyond the returned length. !!!
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
