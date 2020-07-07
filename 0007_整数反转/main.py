#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        is_negetive = x < 0
        if is_negetive:
            x = -x
        new_x = 0
        while x:
            new_x = new_x * 10 + x % 10
            x //= 10
        if new_x > 2**31:
            return 0
        return -new_x if is_negetive else new_x