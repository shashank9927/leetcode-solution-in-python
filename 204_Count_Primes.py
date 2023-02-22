import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        li=[1]*(n)
        li[0]=0
        li[1]=0
        #c=n-2
        for i in range(2,int(math.sqrt(n))+1):
            if li[i]==1:
                for j in range(i*i,n,i):
                    li[j]=0
                    
        return sum(li)

        
