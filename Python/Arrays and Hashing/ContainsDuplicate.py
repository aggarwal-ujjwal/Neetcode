class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #ans = False;

        seen = {};

        for num in nums:
            if num in seen and seen[num] >= 1:
                return True;
            seen[num] = seen.get(num, 0) + 1
        return False;



#define bool - with uppercase first letter - True and False
#get function on dictionary

# Creating a default dictionary with integer value 0
#->  count = defaultdict(int)