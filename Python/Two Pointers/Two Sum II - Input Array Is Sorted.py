class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i=0
        j=n-1
        #Can be written as i,j=0,n-1
        ans=[]
        while (i<j):
            if (numbers[i]+numbers[j]==target):
                ans.append(i+1);
                ans.append(j+1);
                return ans
            elif (numbers[i]+numbers[j]<target):
                i+=1
            else:
                j-=1
        return ans


#Solution