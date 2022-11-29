class Student:
    number_of_students = 0

    def __init__(self, first, last, score):
        self.first = first
        self.last = last
        self.score = score
        Student.number_of_students += 1
    
    def __str__(self):
        result = f"{self.first:>10s}{self.last:>10s}{self.score:10.2f}"
        return result

def main():
    filename = input("Enter the input filename: ")
    name_file = open(filename, 'r')
    students = []
    total = 0
    average = 0

    for line in name_file:
        items = line.rstrip().split()
        grade = float(items[2])
        student = Student(items[0], items[1], grade)
        students.append(student)
        total += grade
    name_file.close()
    
    if Student.number_of_students > 0:
        average = total / Student.number_of_students
    print(f"Average grade is {average:.2f}")

    print("Students with grades > average")
    print(f"{'First':>10s}{'Last':>10s}{'Score':>10s}")
    for student in students:
        if student.score > average:
            print(student)

if __name__ == "__main__":
    main()
