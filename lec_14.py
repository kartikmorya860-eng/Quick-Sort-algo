#parameter recursion
class Solution:
    def sumOfSeries(self, n, total, i):
        if i > n:
            print(total)
            return 
        return self.sumOfSeries(n, total + i**3, i + 1)

ob = Solution()
ob.sumOfSeries(5,0,1)

#functional recursion 
# def fun(n):
#                     if n == 1:
#                             return 1
#                     return n + fun(n-1) 
# print(fun(4))