#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for s in zip(*strs):
            if (s[0],) * len(s) == s:
                result += s[0]
            else:
                break
        return result