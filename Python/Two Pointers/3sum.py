#inefficient solution, not int ans will take a lot of time when it grows bigger so use last seen

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums = sorted(nums)
        n = len(nums)
        ans = []

        if (n<3 or nums[0]>0):
            return ans

        hmap={}
        for i,num in enumerate(nums):
            hmap[nums[i]]=i

        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):

                if -(num1+num2) in hmap:
                    k = hmap[-(num1+num2)]
                    if(i!=j and j!=k and i!=k):
                        triplet = sorted([num1,num2,-(num1+num2)])
                        if triplet not in ans:
                            ans.append([num1,num2,-(num1+num2)])

        return ans

#sol 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums = sorted(nums)
        n = len(nums)
        ans = []

        if (n<3 or nums[0]>0):
            return ans

        hmap={}
        for i,num in enumerate(nums):
            hmap[nums[i]]=i

        seen_triplets = set()

        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):

                if i < j:
                    target = -(num1 + num2)
                    if target in hmap:
                        k = hmap[target]

                        if j < k:
                            triplet = [num1, num2, target]

                            if tuple(triplet) not in seen_triplets:
                                ans.append(triplet)
                                seen_triplets.add(tuple(triplet))

        return ans








