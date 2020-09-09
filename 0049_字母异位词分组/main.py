# https://leetcode.com/problems/group-anagrams/

'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

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