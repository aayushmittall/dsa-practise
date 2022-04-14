from functools import lru_cache
@lru_cache
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

# class Solution:
#     def climbStairs(self, n):
#         one=two=1 
#         for _ in range(n):
#             one,two=two,one+two
#         return one
