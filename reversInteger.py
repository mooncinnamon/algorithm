class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            number = str(x)[::-1]
        elif x < 0:
            number = "-" + str(x)[1:][::-1]
        return int(number) if -2 ** 31 < int(number) < 2 ** 31 else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(1534236469))
