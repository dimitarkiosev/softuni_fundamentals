import math

students = int(input())
lectures = int(input())
bonus = int(input())

total_bonus = 0
student_at = 0
for i in range(students):
    n = int(input())
    n_bonus = n / lectures * (5 + bonus)
    if n_bonus >= total_bonus:
        total_bonus = n_bonus
        student_at = n

print(f'Max Bonus: {math.ceil(total_bonus)}.')
print(f'The student has attended {student_at} lectures.')
