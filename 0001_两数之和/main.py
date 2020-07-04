#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums: List[int], target: int):
        hash_map = dict()
        for index, x in enumerate(nums):
            if target - x in hash_map:
                return [index, hash_map[target - x]]
            hash_map[x] = index