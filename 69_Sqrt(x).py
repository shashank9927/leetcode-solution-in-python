#using binary search method

class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        mid=(left+right)//2
        
        while left<=right:
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
            mid=(left+right)//2
        return mid
