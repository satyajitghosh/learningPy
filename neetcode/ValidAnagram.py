'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {str:int}
        dict_t = {str:int}

        for chr in s:
            if chr in dict_s:
                dict_s[chr] += 1
            else:
                dict_s[chr] = 1
        
        for chr in t:
            if chr in dict_t:
                dict_t[chr] += 1
            else:
                dict_t[chr] = 1

        return dict_s==dict_t