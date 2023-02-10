#Finding valid perfect square using binary search method

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=0
        right=num
        mid=(left+right)//2

        while left<=right:
            if mid*mid==num:
                return True
            elif mid*mid<num:
                left=mid+1
            else:
                right=mid-1
            mid=(left+right)//2
        
        return False
