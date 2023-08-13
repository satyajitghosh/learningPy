'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open,close):
            if open==n  and close==n:
                res = "".join(stack)
                result.append(res)
                return 
            if open < n:
                stack.append('(')
                backtrack(open+1,close)
                stack.pop()
            if close < open:
                stack.append(')')
                backtrack(open,close+1)
                stack.pop()
        
        backtrack(0,0)
        return result
