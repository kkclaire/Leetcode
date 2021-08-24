# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# class Solution(object):

#     # method 1: use carry
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         N = len(digits)
#         pos = N - 1
#         carry = 0
#         digits[-1] += 1

#         while pos >= 0:
#             digits[pos] += carry
#             if digits[pos] >= 10:
#                 digits[pos] -= 10
#                 carry = 1
#             else:
#                 carry = 0
#             pos -= 1

#         if carry:
#             digits.insert(0, 1)
#         return digits


class Solution(object):

    # method 2: find 9
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            print("position is:", i, " --> digits is:", digits[i])
            if digits[i] == 9:
                digits[i] = 0
                print("9 is add: ", digits)
            else:
                digits[i] += 1
                print('what: ', digits)
                return digits

        digits[0] = 1
        digits.append(0)
        return digits


test = Solution()
print(test.plusOne([9, 9, 9]))
