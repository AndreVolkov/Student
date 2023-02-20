# Student
class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_score = []
    def add_score(self, exam_score):
        self.exam_score = exam_score
        pass
    def show_scores(self):  
            print('Show scores:', str(self.exam_score).strip('[]'))

    def score_average(self):
        if self.exam_score != []:
            print(f"Average score: {sum(self.exam_score)/len(self.exam_score):.2f}")
        else:
            print('The student has not yet passed any exam')
        pass
    def course_passed(self):
        k = 0
        for i in self.exam_score:
            if i > 60:
                k = k +1
        if k == 3:
            return True
            
        else:
            return False
        
    def printStudent(self):
        print("Name:", self.first_name, self.last_name)
        print("ID:", self.student_id)
# 1, John, Doe, [100, 95]
s = Student(1, 'John', 'Doe')
s.printStudent()
#exam_score = list( map(int, input().split()) )
exam_score = [100, 95]
s.add_score(exam_score)    
s.show_scores()
s.score_average()
print(s.course_passed())
# 2, Linda, Jones, [25, 65, 80, 75]
l = Student(2, 'Linda', 'Jones')
l.printStudent()
l.show_scores()
l.score_average()
exam_score = [25, 65, 80, 75]
l.add_score(exam_score)
l.show_scores()
l.score_average()
print(l.course_passed())
# 3, Jason, Kirk, [50, 60, 55]
j = Student(3, 'Jason', 'Kirk')
j.printStudent()
j.add_score([50, 60, 55])
j.show_scores()
j.score_average()
print(j.course_passed())
# 4, Jane, Doe, [95, 80, 100]
d = Student(4, 'Jane', 'Doe')
d.printStudent()
d.exam_score = [95, 80, 100]
d.show_scores()
d.score_average()
print(d.course_passed())

