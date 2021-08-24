#  Largest Number At Least Twice of Others

# in a given integer array nums, there is always exactly one largest element.
# Find whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, otherwise return -1.

# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99]


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        if len(nums) == 1:
            return -1
        largest = max(nums)
        ind = nums.index(largest)
        nums.sort()
        if largest >= 2 * nums[-2]:
            return ind
        else:
            return -1


test = Solution()
print(test.dominantIndex([0, 0, 0, 1]))
