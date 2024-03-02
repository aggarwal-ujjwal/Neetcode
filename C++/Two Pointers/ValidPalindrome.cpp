class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        //int i=0 ; j =n-1;
        for (int i = 0, j = n - 1; i < j; i++, j--) { // Move 2 pointers from each end until they collide
        while (isalnum(s[i]) == false && i < j) i++; // Increment left pointer
        while (isalnum(s[j]) == false && i < j) j--; // Decrement right pointer
        if (toupper(s[i]) != toupper(s[j])) return false;
    }
    return true;
    }
}; //isalnum imp - tolower and toupper as well