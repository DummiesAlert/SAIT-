class Person:
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self):
        return f"name is {self.name}, age is {self.age}"


def main():
    person_list = []
    read_persons_file(person_list)
    for p in person_list:
        print(p)

    person_info = input("Enter name and age (separated by a space): ")
    while person_info != "":
        items = person_info.split()
        name = items[0]
        age = int(items[1])
        person = Person(name, age)
        person_list.append(person)
        person_info = input("Enter name and age (separated by a space): ")

    for p in person_list:
        print(p)
    write_persons_file(person_list)


def read_persons_file(p_list):
    p_file = open(r"c:\temp\persons.txt", "r")
    for p_line in p_file:
        p_items = p_line.rstrip().split()
        person = Person(p_items[0], p_items[1])
        p_list.append(person)
    p_file.close()


def write_persons_file(p_list):
    p_file = open(r"c:\temp\persons.txt", "w")
    for person in p_list:
        p_file.write(person.name + " " + str(person.age) + "\n")
    p_file.close()


if __name__ == "__main__":
    main()
