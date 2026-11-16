class Solution:
    def thirdMax(self, arr: list[int]) -> int:
        a=b=c=float('-inf')
        for i in arr:
            if i>a:
                c=b
                b=a
                a=i
            if i<a and i>b:
                c=b
                b=i
            if i<b and i>c:
                c=i
        if c==float('-inf'):
            return a
        else:
             return c        


        