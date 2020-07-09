#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def myAtoi(self, str: str) -> int:
        new_str = str.strip().split(' ')[0]
        result_str = ''
        for index,i in enumerate(new_str):
            if i.isdigit() or (index == 0 and i in ['-', '+']):
                result_str += i
            else:
                break
        try:
            result = int(result_str)
        except:
            return 0
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result