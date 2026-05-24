class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row, target):
            l = 0
            r = len(row) - 1

            while l <= r:
                mid = (l + r) // 2

                if target > row[mid]:
                    l = mid + 1
                elif target < row[mid]:
                    r = mid - 1
                else:
                    return True
            return False

        

        if len(matrix) == 1:
            return binary_search(matrix[0], target)

        if len(matrix[0]) == 1:
            for i in matrix:
                if i[0] == target:
                    return True
            return False

        if matrix == []:
            return False

        row_len = len(matrix[0]) - 1
        col_len = len(matrix) - 1
        col = 0

        print(row_len, col_len)

        for row in matrix: 
            if target < row[0]:
                return False
            if target == row[0]:
                return True
            if target > row[0]:
                if target == row[row_len]:
                    return True
                if target > row[row_len] and col == col_len:
                    return False
                if target < row[row_len]:
                    return binary_search(row, target)
            col += 1