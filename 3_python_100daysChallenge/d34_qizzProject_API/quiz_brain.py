import html 
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    ## just get the T or F derectly, no need to set a n argument like if else... 


    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number +=1
        q_text = html.unescape(self.current_question.text)
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score +=1

        else:
            print("Wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"corrent score is: {self.score}/{self.question_number}")
        print("\n")


