class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        
        prefixSum = [0] * (n + 1)

        
        prefixCount = [0] * (n + 1)

        
        prefixNum = [0] * (n + 1)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        
        for i in range(n):
            digit = int(s[i])

            prefixSum[i + 1] = prefixSum[i]
            prefixCount[i + 1] = prefixCount[i]
            prefixNum[i + 1] = prefixNum[i]

            if digit != 0:
                prefixSum[i + 1] += digit
                prefixCount[i + 1] += 1
                prefixNum[i + 1] = (prefixNum[i] * 10 + digit) % MOD

        ans = []

        for l, r in queries:

            
            totalSum = prefixSum[r + 1] - prefixSum[l]

            if totalSum == 0:
                ans.append(0)
                continue

    
            leftCnt = prefixCount[l]

        
            totalCnt = prefixCount[r + 1] - prefixCount[l]

            
            x = (
                prefixNum[r + 1]
                - prefixNum[l] * pow10[totalCnt]
            ) % MOD

            ans.append((x * totalSum) % MOD)

        return ans