class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        seq = 0
        nums = set(nums)  #O(n) operation

        for num in nums:
            if (num-1) not in nums:     #imp one to make sure already counted ones are not included
                seq = num + 1;
                while seq in nums:
                    seq += 1;
                best = max(best, seq-num)

        return best
