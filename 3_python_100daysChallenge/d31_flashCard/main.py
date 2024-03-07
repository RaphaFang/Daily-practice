from tkinter import*
import pandas
import random
import time
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

# 讀取資料
data = pandas.read_csv("3_python_100daysChallenge/d31_flashCard/data/french_words.csv")

# 這步驟是為了，學習過的資料不會再下次開始時，重新出現
try:
    data = pandas.read_csv("d31_flashCard/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("3_python_100daysChallenge/d31_flashCard/data/french_words.csv")
    data_dict = original_data.to_dict(orient= "records")
else:
    data_dict = data.to_dict(orient= "records")

# func--------------------------------------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image=card_back_img)

def list_to_csv():
    global current_card
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("d31_flashCard/data/words_to_learn.csv", index=False)
    ## index=False, will make the csv data without index.
    next_card()

# window--------------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# code--------------------------------------------------------------
# 主要的背景圖片
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="3_python_100daysChallenge/d31_flashCard/images/card_front.png")
card_back_img = PhotoImage(file="3_python_100daysChallenge/d31_flashCard/images/card_back.png")

canvas_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# 叉叉按鈕
cross_image = PhotoImage(file="3_python_100daysChallenge/d31_flashCard/images/wrong.png")
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0 )
# 打勾按鈕
check_image = PhotoImage(file="3_python_100daysChallenge/d31_flashCard/images/right.png")
known_btn = Button(image=check_image, highlightthickness=0, command=list_to_csv)
known_btn.grid(row=1, column=1 )

next_card()
# 為了讓初始沒點擊任何按鈕時也有字卡

window.mainloop()