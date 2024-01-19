class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums.sort();
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        print(hashmap)
        #Sort the dictionary items based on frequency in descending order.
        sorted_hmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        print(type(sorted_hmap)) #This returns a list
        ans = []
        for i in range(k):
            ans.append(sorted_hmap[i][0])
            # # ans.append(hashmap[i][0]) didnt work(If you encountered an error when using hashmap[i][0], it's likely because hashmap is a dictionary, and dictionaries don't support indexing with integers like lists do.)
            # In your loop, sorted_hmap[i] gives you the i-th tuple from the sorted list. To get the key from that tuple, you should use sorted_hmap[i][0]. If you were using hashmap[i][0], it would attempt to access the i-th element of the dictionary, which doesn't make sense because dictionaries are not ordered and don't have integer indices.)
        return ans


# lambda item: item[1]: This creates a lambda function that takes an item as input (in this case, a key-value pair), and it returns item[1], which is the value associated with the key.
# So, when you use key=lambda item: item[1] in the sorted() function, you are telling it to sort the elements based on the values (second element) of each item.