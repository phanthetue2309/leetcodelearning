# https://leetcode.com/problems/two-sum/description/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_final = []
        while not array_final:
            max_number = max(nums)
            max_number_index = nums.index(max_number)
            nums[max_number_index] = -100
            find_value = target - max_number
            if find_value in nums:
                find_value_index = nums.index(find_value)
                array_final = [max_number_index, find_value_index]
        return sorted(array_final)


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum(nums=[2, 7, 11, 15], target=9)
    print(result)
