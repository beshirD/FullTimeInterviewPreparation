class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix) == 0:
            return matrix
        result = []
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        size = len(matrix) * len(matrix[0])
        while len(result) < size:
            if len(result) < size:
                for i in range(left,right+1):
                    result.append(matrix[top][i])
                top += 1
            if len(result) < size:
                for i in range(top,bottom+1):
                    result.append(matrix[i][right])

                right -= 1
            if len(result) < size:
                for i in range(right, left-1 , -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if len(result) < size:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1
        return result
            