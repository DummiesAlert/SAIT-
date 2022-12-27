def main():
    filename = input("Enter the input filename: ")
    name_file = open(filename, 'r')
    first_name = []
    last_name = []
    score = []
    total = 0
    average = 0 #C:\SAIT\CPRG216S

    for line in name_file:
        items = line.rstrip().split()
        first_name.append(items[0])
        last_name.append(items[1])
        grade = float(items[2])
        score.append(grade)
        total += grade
    name_file.close()
    
    if len(score) > 0:
        average = total / len(score)
    print(f"Average grade is {average:.2f}")

    print("Students with grades > average")
    print(f"{'First':>10s}{'Last':>10s}{'Score':>10s}")
    for i in range(len(score)):
        if score[i] > average:
            print(f"{first_name[i]:>10s}{last_name[i]:>10s}{score[i]:10.2f}")

if __name__ == "__main__":
    main()