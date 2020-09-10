#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for i in strs:
            i_key = tuple(sorted(i))
            if i_key in result_dict:
                result_dict[i_key].append(i)
            else:
                result_dict[i_key] = [i,]
        return list(result_dict.values())