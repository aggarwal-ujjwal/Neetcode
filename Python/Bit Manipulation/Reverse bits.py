class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0
        for i in range(0,32):
            ans = (ans<<1) + (n>>i & 1)

        return ans

# The problem lies with the order of operations in the line ans = ans<<1 + (n>>i & 1).
# The << operator has higher precedence than the + operator.
# To ensure that the left shift operation is performed before the addition,
# you need to use parentheses to group the operations properly.
