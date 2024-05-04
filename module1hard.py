grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3],
          [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_alph = []
for i in range(len(students)):
    students_alph.append(min(students))
    students.remove(min(students))

grades_sum = []
for i in range(len(grades)):
    grades_sum.append(sum(grades[i])/len(grades[i]))

tabel = zip(students_alph,grades_sum)

print(dict(tabel))
