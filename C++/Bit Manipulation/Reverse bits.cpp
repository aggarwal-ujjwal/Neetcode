class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans=0 , last;

        for(int i = 0 ; i<32 ; i++){
            ans = (ans<<1) + (n>>i &1);
        }
      return ans;
    }
};


// In each iteration, it shifts ans to the left by 1 bit (ans << 1) to make space for the next bit.
// It then extracts the rightmost bit of n by right-shifting n by i bits and performing a bitwise AND operation with 1 (n >> i & 1).
// This operation effectively checks if the ith bit of n is set or not.