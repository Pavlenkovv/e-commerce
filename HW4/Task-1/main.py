import group
import student


class GroupNotMoreThan10(Exception):
    """The group_list cannot be more than 10 people"""

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


if __name__ == '__main__':
    stud1 = student.Student('Ivanenko', 'Ivan', 20, 95)
    stud2 = student.Student('Prokopenko', 'Milana', 19, 90)
    stud3 = student.Student('Proko', 'Mila', 21, 85)
    stud4 = student.Student('Prokopen', 'Misha', 19, 80)
    stud5 = student.Student('Furza', 'Milana', 18, 75)
    stud6 = student.Student('Furza2', 'Milana', 18, 75)
    stud7 = student.Student('Furza3', 'Milana', 18, 75)
    stud8 = student.Student('Furza4', 'Milana', 18, 75)
    stud9 = student.Student('Furza5', 'Milana', 18, 75)
    stud10 = student.Student('Furza6', 'Milana', 18, 75)
    stud11 = student.Student('Furza7', 'Milana', 18, 75)
    group_1 = group.Group()
    group_1.add_to_group(stud1)
    group_1.add_to_group(stud2)
    group_1.add_to_group(stud3)
    group_1.add_to_group(stud4)
    group_1.add_to_group(stud5)
    group_1.add_to_group(stud6)
    group_1.add_to_group(stud7)
    group_1.add_to_group(stud8)
    group_1.add_to_group(stud9)
    group_1.add_to_group(stud10)
    # group.add_to_group(stud11)
    print(group_1)
    print('*' * 80)
    group_1.remove_from_group(stud2)
    print(group_1)
    print('Id student is: ', group_1.search(stud4))
