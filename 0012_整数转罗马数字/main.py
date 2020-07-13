#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        其实用到了一个进制的概念，很妙
        """
        return_str = ""
        pair = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
                900: "CM", 1000: "M"}
        for key in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            return_str += pair[key] * (num // key)
            num = num % key
        return return_str
