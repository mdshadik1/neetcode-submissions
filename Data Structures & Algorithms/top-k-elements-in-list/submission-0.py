class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1

        
        items = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        
        ans = []
        for i in range(k):
            ans.append(items[i][0])

        return ans

        


                 



