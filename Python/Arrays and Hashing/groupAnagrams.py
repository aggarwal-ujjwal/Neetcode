class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list);  #Initialize hashmap of lists
        for stemp in strs:
            res = ''.join(sorted(stemp))
            #print(res);
            if res in hashmap:
                hashmap[res].append(stemp)
                #print("if-",stemp)
            else:
                hashmap[res].append(stemp)
                #print("else-",stemp)
        #print(hashmap)
        ans = []  #initialize list of lists
        for key,value in hashmap.items():  #iterate hashmap of lists
            ans.append(value)

        return ans



#from collections import defaultdict

# Create a defaultdict with lists as default values
#hashmap_of_lists = defaultdict(list)


# Iterate over the hashmap of lists
#for key, values in hashmap_of_lists.items():
#    print(f"Key: {key}, Values: {values}")