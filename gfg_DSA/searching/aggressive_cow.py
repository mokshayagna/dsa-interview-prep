class Solution:
    def is_valid(self, stalls, k, n, mid):
        cows = 1
        last_pos = stalls[0]

        for i in range(1, n):
            if stalls[i] - last_pos >= mid:
                cows += 1
                last_pos = stalls[i]

            if cows == k:
                return True

        return False

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)

        start = 1
        end = stalls[n - 1] - stalls[0]
        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if self.is_valid(stalls, k, n, mid):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans


def main():
    stalls = [1, 2, 4, 8, 9]
    k = 3

    obj = Solution()
    result = obj.aggressiveCows(stalls, k)

    print("Largest minimum distance between cows:", result)


if __name__ == "__main__":
    main()