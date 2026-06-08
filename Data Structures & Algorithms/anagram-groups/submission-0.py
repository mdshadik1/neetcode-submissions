class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for i in strs:
            key = ''.join(sorted(i))

            if key in mp:
                mp[key].append(i)
            else:
                mp[key] = [i] #frequecy wala case 

        return list(mp.values())
