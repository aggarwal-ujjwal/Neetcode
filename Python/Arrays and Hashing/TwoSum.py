# Ue this when you need both inde and value in pyhitn for loop
# Use the built-in function enumerate():
#
# for idx, x in enumerate(xs):
#     print(idx, x)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {};

        for i,num in enumerate(nums):
            temp[num]=i;

        print(temp)
        for i,num in enumerate(nums):
            if (target-num) in temp and temp[target-num]!=i:
                return [temp[target-num],i];
