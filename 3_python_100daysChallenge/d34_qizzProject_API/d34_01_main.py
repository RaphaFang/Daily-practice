from question_model import Question
from d34_02_data import question_data
<<<<<<< HEAD
from d34_03_quiz_brain import QuizBrain
from d34_04_ui import QuizInterFace
=======
from quiz_brain import QuizBrain
>>>>>>> 0636eb7 (first commit)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
<<<<<<< HEAD
quiz_ui = QuizInterFace()

# while quiz.still_has_questions():
#     quiz.next_question()
=======

while quiz.still_has_questions():
    quiz.next_question()
>>>>>>> 0636eb7 (first commit)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

<<<<<<< HEAD
 
=======
>>>>>>> 0636eb7 (first commit)
