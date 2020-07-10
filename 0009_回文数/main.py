#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        low_index = 0
        high_index = len(x_str) - 1
        while low_index < high_index:
            if x_str[low_index] == x_str[high_index]:
                low_index += 1
                high_index -= 1
            else:
                return False
        return True