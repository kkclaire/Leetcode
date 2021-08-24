class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: list[int]
        :type val: int
        :rtype: int
        """

        # now = 0
        # last = len(nums) - 1

        # while now <= last:
        #     if nums[now] == val:
        #         nums[now], nums[last] = nums[last], nums[now]
        #         last -= 1
        #     else:
        #         now += 1

        # return last + 1

        slow = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow


a = Solution()
print(a.removeElement([3, 2, 2, 3], 3))
