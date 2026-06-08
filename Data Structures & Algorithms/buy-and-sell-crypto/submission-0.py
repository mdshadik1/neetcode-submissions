class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=float('inf')

        maxx=0
        for i in prices:
            if i<minn:
                minn=i
            else:
                profit=i-minn
                maxx=max(maxx,profit)
        return maxx
