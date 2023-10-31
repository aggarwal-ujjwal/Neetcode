class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        if sorted_s!=sorted_t :
            return False;
        return True;


#sort a string in python
#check in-place sorting as well
