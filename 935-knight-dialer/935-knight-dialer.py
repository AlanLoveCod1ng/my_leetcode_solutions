class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9+7
        dp = [1]*10
        if n == 1:
            return 10
        dp[5] = 0
        table = {1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4],0:[4,6]}
        prev_dp = dp.copy()
        dp = [0]*10
        for i in range(1,n):
            for j in range(0,10):
                prevPos = table[j]
                for z in prevPos:
                    dp[j] = (dp[j] + prev_dp[z])%mod
            prev_dp = dp
            dp = [0]*10
        return sum(prev_dp)%mod