class Solution:
    def solve(self, matrix):
        d = 0
        top = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        c = 0
        res = []
        direction = 0
        while top <= down and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
                
            if direction == 1:
                for i in range(top, down + 1):
                    res.append(matrix[i][right])
                right -= 1
                
            if direction == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
                
            if direction == 3:
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
            direction = (direction + 1) % 4
        return res
         
ob = Solution()
matrix = [
    [7, 10, 9],
    [2, 9, 1],
    [6, 2, 3],
    [9, 1, 4],
    [2, 7, 5],
    [9, 9, 11]
]
print(ob.solve(matrix))
