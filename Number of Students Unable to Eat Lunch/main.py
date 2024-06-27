import sys

sys.path.append("..")

from typing import Tuple, List, Any


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    student_q = [i for i in students]
    sandwitch_s = [i for i in sandwiches]
    student_reject_count = 0

    while sandwitch_s and student_reject_count != len(student_q):
        student = student_q.pop(0)

        if student == sandwitch_s[0]:
            student_reject_count = 0
            sandwitch_s.pop(0)
            continue

        student_q.append(student)
        student_reject_count += 1

    return len(student_q)


if __name__ == "__main__":
    testcases: List[Tuple[List[int], List[int], int]] = [
        ([1, 1, 0, 0], [0, 1, 0, 1], 0),
        ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
    ]

    assert all(
        countStudents(students, sandwitches) == expected
        for students, sandwitches, expected in testcases
    )
