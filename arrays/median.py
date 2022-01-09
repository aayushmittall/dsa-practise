# https://practice.geeksforgeeks.org/problems/find-the-median0527/1#

class Solution:
    """
        input : v -> list
    """

    def find_median(self, v):
        v.sort()
        n = len(v)
        x = n//2
        if (n % 2 == 0):
            a = v[x-1] + v[x]
            return a//2
        else:
            return v[x]


if __name__ == "__main__":
    arr = [1, 3, 4, 6, 2, 5]
    sol = Solution()
    median = sol.find_median(arr)
    print(median)
