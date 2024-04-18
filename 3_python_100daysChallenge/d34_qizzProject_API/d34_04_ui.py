THEME_COLOR = "#375362"
from tkinter import *


class QuizInterFace:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                      125,
                                                        text="question text",
                                                          fill=THEME_COLOR,
                                                          font=("Arial", 20 , "italic"))
        # be aware that, you should always give a x, y position for text on canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="3_python_100daysChallenge/d34_qizzProject_API/images/true.png")
        false_img = PhotoImage(file="3_python_100daysChallenge/d34_qizzProject_API/images/false.png")
        
        self.true_button = Button(image=true_img, highlightthickness=0) 
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)



        
        self.window.mainloop()