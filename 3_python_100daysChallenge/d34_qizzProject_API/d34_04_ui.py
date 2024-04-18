THEME_COLOR = "#375362"
from tkinter import *
from d34_03_quiz_brain import QuizBrain

# Type Hint
# 309. 可以定義變數的「type」， age = int  /  name = str
# 如下方 quiz_brain:QuizBrain
# 也可以在func 後面加上 def a_unc() -> bool
# 來標記這個func 應該 return 的東西 
class QuizInterFace:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                      125,
                                                      width=280,
                                                        text="question text",
                                                          fill=THEME_COLOR,
                                                          font=("Arial", 20 , "italic"))
        # be aware that, you should always give a x, y position for text on canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="3_python_100daysChallenge/d34_qizzProject_API/images/true.png")
        false_img = PhotoImage(file="3_python_100daysChallenge/d34_qizzProject_API/images/false.png")
        
        self.true_button = Button(image=true_img, highlightthickness=0, command = self.true_pressed()) 
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed())
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
          self.score_label.config(text=f"Score: {self.score}")
          q_text = self.quiz.next_question()
          self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "Game Ends")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
#  line 48 & 51 do the same thing
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)
        
