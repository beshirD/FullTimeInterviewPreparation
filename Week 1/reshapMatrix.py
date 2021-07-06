class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        new_mat = [[0] * c for _ in range(r)]
        
        for i in range(m):
            for j in range(n):
                el_rank = i * n + j
                new_row = el_rank // c
                new_col = el_rank % c
                new_mat[new_row][new_col] = mat[i][j] 
        
        return new_mat
    
#     def iterator(self, mat):
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 yield mat[i][j]