'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".




argh....test cases contains Upper Case.. it wasn't clear in the question
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        ss = list(s)
        i,j = 0, len(s)-1
        while i < j:
            while(ss[i] not in vowels and i < j):
                i+=1
            while(ss[j] not in vowels and i < j):
                j-=1
            ss[i],ss[j] = ss[j],ss[i]
            i+=1
            j-=1
        return ''.join(ss)