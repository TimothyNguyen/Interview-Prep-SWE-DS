'''
Given a string s that contains parentheses 
and letters, remove the minimum number of 
invalid parentheses to make the input string 
valid.

Return all the possible results. You may return the 
answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

O(2^n) time
O(n) space
'''
from typing import List, Optional


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.len_longest_str = -1
        self.res = set()

        def dfs(curr_path: List[Optional[str]], curr_idx: int, l: int, r: int):
            if curr_idx >= len(s):
                if l == r:
                    if len(curr_path) > self.len_longest_str:
                        self.len_longest_str = len(curr_path)
                        self.res = set()
                        self.res.add("".join(curr_path))
                    elif len(curr_path) == self.len_longest_str:
                        self.res.add("".join(curr_path))
            else:
                ch = s[curr_idx]
                if ch == '(':
                    dfs(curr_path, curr_idx + 1, l, r)
                    curr_path.append(ch)
                    dfs(curr_path, curr_idx + 1, l + 1, r)
                    curr_path.pop()
                elif ch == ')':
                    dfs(curr_path, curr_idx + 1, l, r)
                    if l > r:
                        curr_path.append(ch)
                        dfs(curr_path, curr_idx + 1, l, r + 1)
                        curr_path.pop()
                else:
                    curr_path.append(ch)
                    dfs(curr_path, curr_idx + 1, l, r)
                    curr_path.pop()

        dfs([], 0, 0, 0)
        return list(self.res)