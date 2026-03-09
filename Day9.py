//3129. Find All Possible Stable Binary Arrays I
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        L = limit + 1

        # Swapping 0 and 1 doesn't change the count, but can reduce memory (O(one*L))
        if one > zero:
            zero, one = one, zero

        # First row
        dp0_prev, dp1_prev = [0] * (one + 1), [0] * (one + 1)
        for j in range(1, min(one, limit) + 1):
            dp1_prev[j] = 1

        # Store last L = limit + 1 dp1 rows to access dp1[i-L][j]
        dp1q = deque([dp1_prev[:]])
        for i in range(1, zero + 1):
            dp0, dp1 = [0] * (one + 1), [0] * (one + 1)
            if i <= limit:
                dp0[0] = 1

            for j in range(1, one + 1):
                dp0[j] = (dp0_prev[j] + dp1_prev[j] - (dp1q[0][j] if i >= L else 0)) % mod
                dp1[j] = (dp0[j - 1] + dp1[j - 1] - (dp0[j - L] if j >= L else 0)) % mod

            dp1q.append(dp1[:])
            if len(dp1q) > L:
                dp1q.popleft()

            dp0_prev, dp1_prev = dp0, dp1

        return (dp0_prev[one] + dp1_prev[one]) % mod
