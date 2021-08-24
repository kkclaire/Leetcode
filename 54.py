class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            for j in reversed(range(left, right)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result


result = Solution()
print(result.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8,], [9, 10, 11, 12], [13, 14, 15, 16], [17,18,19,20],]))
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            for j in reversed(range(left, right)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result


result = Solution()
#print(result.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8,], [9, 10, 11, 12], [13, 14, 15, 16], [17,18,19,20],]))
