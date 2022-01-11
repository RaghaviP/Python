class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.subject = self.subject()

    def show(self):
        print(self.name, self.rollno)
        self.subject.show()

    class subject:

        def __init__(self):
            self.subject = ('Mathematics','Science')
            self.marks = 56, 95

        def show(self):
            print(self.subject, self.marks)

s1 = Student('Ria', 58)
s2 = Student('Tina', 52)

s1.show()