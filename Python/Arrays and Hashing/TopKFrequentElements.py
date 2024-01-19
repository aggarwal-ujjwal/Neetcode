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

        ans = []
        for i in range(k):
            ans.append(sorted_hmap[i][0])

        return ans


# lambda item: item[1]: This creates a lambda function that takes an item as input (in this case, a key-value pair), and it returns item[1], which is the value associated with the key.
# So, when you use key=lambda item: item[1] in the sorted() function, you are telling it to sort the elements based on the values (second element) of each item.