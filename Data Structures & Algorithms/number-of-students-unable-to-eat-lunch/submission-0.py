class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_round = 0
        students_square = 0

        for i in students:
            if i == 0:
                students_round += 1
            elif i == 1:
                students_square += 1

        for s in sandwiches:
            if s == 0:
                if students_round > 0:
                    students_round -= 1
                else:
                    break
            elif s == 1:
                if students_square > 0:
                    students_square -= 1
                else:
                    break
        
        return students_round + students_square