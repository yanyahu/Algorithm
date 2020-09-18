#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 动态规划，从底层向上递推
        if not triangle:
            return 0
        result = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                result[j] = min(result[j], result[j + 1]) + triangle[i][j]
        return result[0]