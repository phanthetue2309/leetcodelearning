# do by myself
# 2024-02-11-Tue
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -int(str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])

        if not -(pow(2, 31)) <= x <= (pow(2, 31) - 1):
            x = 0
        return x


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverse(x=1534236469)
    print(result)
