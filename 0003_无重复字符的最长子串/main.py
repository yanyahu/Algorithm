#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dict = {}
        slow = 0
        max_count = 0
        for index, i in enumerate(s):
            if i in str_dict and str_dict[i] >= slow:
                slow = str_dict[i] + 1
            str_dict[i] = index
            if index - slow + 1 > max_count:
                max_count = index - slow + 1
        return max_count