Student class with instance variables:

student_id: int
first_name: str
last_name: str
exam_scores: list[int]
The constructor takes student_id, first_name, and last_name in order to initialize the class. The exam_scores must be initialized as an empty list.

and the methods:

add_score(score): adds score to the list exam_scores. The score is any number in [0, 100]
show_scores(): displays all student scores in one row
score_average(): returns student's average score, or prints a message that the student didn't pass any exam yet
course_passed(): if student collects three scores > 60, the method returns True, else method returns False
Test your program for students listed below:

1, John, Doe, [100, 95] 2, Linda, Jones, [25, 65, 80, 75] 3, Jason, Kirk, [50, 60, 55] 4, Jane, Doe, [95, 80, 100]