class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in mp:
                mp[key].append(i)
            else:
                mp[key] = [i]
        return list(mp.values())