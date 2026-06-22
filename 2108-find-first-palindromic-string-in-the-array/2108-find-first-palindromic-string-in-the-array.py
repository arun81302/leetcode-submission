class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            temp=i
            temp=temp[::-1]
            if temp==i:
                return i
        return ""