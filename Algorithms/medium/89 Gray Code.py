'''

The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.

 

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: n = 1
Output: [0,1]
 

Constraints:

0 <= n <= 15

'''

from typing import List

# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         code = ['0','1']
#         for _ in range(1, n):
#             code = ['0'+ c for c in code]+['1'+ c for c in code[::-1]]
#         return map(lambda x:int(x, 2), code)


class Solution:
    def grayCode(self, n: int) -> List[int]:
        code = [0]
        for _ in range(n):
            code.extend(map(lambda x:x << 1|1, code))
        return code