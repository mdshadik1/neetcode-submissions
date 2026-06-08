class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s:
            if i - 1 not in s:  # start of consecutive sequence
                count = 1
                while i + count in s:
                    count += 1
                longest = max(longest, count)  # update after finishing sequence
        return longest



                

                


        

        