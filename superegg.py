"""
TC: O(k⋅nlogn) k*n sub problems and each take logn to compute
SP: o(k*n)
"""

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dfs(e, f):
            if f <= 1 or e == 1:
                return f
            if (e, f) in memo:
                return memo[(e, f)]
            memo[(e, f)] = float("inf")
            low = 1
            high = f+1
            while low <= high:
                mid = (low + high) // 2
                b = dfs(e - 1, mid - 1)  # Egg breaks
                nb = dfs(e, f - mid)  # Egg does not break

                worst = 1 + max(b, nb)
                memo[(e, f)] = min(memo[(e, f)], worst)

                if b > nb:
                    high = mid - 1  # Move down (we need fewer floors)
                else:
                    low = mid + 1  # Move up (we need more floors)

            return memo[(e, f)]

        return dfs(k, n)
