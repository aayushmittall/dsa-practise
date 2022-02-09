import imp


class Solution:
    def lcs(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        from pprint import pprint
        pprint(dp)
        count = 0
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                pprint(dp)
                count = count+1
                print(count)
        return dp[0][0]


text1 = "india"
text2 = "iia"

res = Solution().lcs(text1, text2)
