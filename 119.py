class Solution(object):
    def getRow(self, rownum):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

# # Method 1: calculate all element

#         # result = [[1 for j in range(i)] for i in range(1, rownum + 1)]
#         # for i in range(2, rownum):
#         #     for j in range(1, i):
#         #         result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
#         # return result

# Method 2:
        result = [1] + [0] * rownum

        for i in range(0, rownum):
            for j in range(i + 1, 0, -1):
                result[j] += result[j - 1]

        return result


result = Solution()
print(result.getRow(3))
