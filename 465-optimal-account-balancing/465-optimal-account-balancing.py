class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:                
        dp = [0]*12
        for i in range(len(transactions)):
            transaction = transactions[i]
            dp[transaction[0]] -= transaction[2]
            dp[transaction[1]] += transaction[2]
        non_zero = []
        for i in range(len(dp)):
            if dp[i] != 0:
                non_zero.append(dp[i])
        
        def dfs(count):
            while count<len(non_zero) and non_zero[count] == 0:
                count+=1
            if count == len(non_zero):
                return 0
            
            r = math.inf
            for i in range(count+1, len(non_zero)):
                if non_zero[i]*non_zero[count]<0:
                    non_zero[i]+=non_zero[count]
                    r = min(r,1+dfs(count+1))
                    non_zero[i]-=non_zero[count]
            return r
                
        return dfs(0)
        

            