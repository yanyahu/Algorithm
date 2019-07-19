# https://leetcode.com/problems/reverse-integer/

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

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