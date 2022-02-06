# https://leetcode.com/problems/find-k-closest-elements/

from re import A
from typing import List


class Solution:

    # time complexity -> O(logn) + k
    def find_closest_element(self, arr: List[int], target: int, window: int) -> List[int]:

        l, r = 0, len(arr)-1

        # closest value
        value, idx = arr[0], 0

        while l <= r:
            m = (l+r)//2
            curr_diff, res_diff = abs(arr[m]-target), abs(value-target)
            if (curr_diff < res_diff or (curr_diff == res_diff and arr[m] < value)):
                value, idx = arr[m], m
            elif arr[m] < target:
                l = m+1
            elif arr[m] > target:
                r = m-1
            else:
                break

        l = r = idx
        for i in range(window-1):
            if l == 0:
                r += 1
            elif (r == len(arr)-1) or (target-arr[l-1] <= arr[r+1]-target):
                l -= 1
            else:
                r += 1
        return arr[l:r+1]

    # Log(n-k) + k
    # Elegant but very difficult to understand
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]


arr = [1, 2, 3, 4, 5, 6]
sol = Solution()
res = sol.find_closest_element(arr, -1, 4), sol.find_closest_element(arr, 4, 5)
print(res)
