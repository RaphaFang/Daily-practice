# # # import tkinter
# from tkinter import *
# # ## only recommend when using "1" class 

# window = Tk()
# window.title("my first GUI program")
# window.minsize(width=500, height=500)

# ## Label
# my_label = Label(text="im not a label", font=("Arial", 24, "bold"))
# my_label.pack()

# # my_label["text"] = "new text"
# my_label.config(text="new text")

# # # some func got's it's default value,
# # # it's optional for you to change the input

# ## Button
# ## you could create a func. once button clicked, the func would be command

# # def btn_clicked():
# #     print("i got clicked")
# #     my_label.config(text = "str")

# def btn_clicked():
#     print("i got clicked")
#     new_t = input1.get()
#     my_label.config(text = new_t)

# button = Button(text="click me.", command=btn_clicked)
# button.pack()
# ## command, not commend

# ## Entry
# input1 = Entry(width=10)
# input1.pack()
# print(input1.get())



# # #2. (250.) _____________________________________________
# # def add(*args):
# #     sum = 0
# #     print(args[0])
# #     ## print the first element in args tuple
# #     for n in args:
# #         sum +=n
# #     return sum
# # print(add)
# # ## by using *args, you can add as much num you want

# # #3. (251.)_____________________________________________
# # def calc(**kwargs):
# #     print(kwargs)
# #     n += kwargs["add"]
# #     n *= kwargs["multiple"]
# #     print(n)
# # ## you can build a "dict" by using **

# # calc(2, add=3, multiple=5)

# # #4. _____________________________________________
# # class Car:
# #     def __init__(self, **kw):
# #         # self.make = kw["make"]
# #         # self.model = kw['model']
# #         ## you'll get error if there is no input in the (e.g. make/model)

# #         self.make = kw.get('make')
# #         self.model = kw.get("model")
# #         ## by using "get" if there is no input in (), it return "none"


# # my_car = Car(make="nissan", model="GTR")
# # print(my_car.model)

# # #5. (below 251.)_____________________________________________

# # def all_aboard(a, *args, **kw): 
# #     print(a, args, kw)
 
# # all_aboard(4, 7, 3, 0, x=10, y=64)
# # ## the output will be
# # ## 4 (7, 3, 0) {"x":10, "y":64}


# window.mainloop()


# dictionary = {
#    'Novel': 'Pride and Prejudice',
#    'year': '1813',
#    'author': 'Jane Austen',
#    'character': 'Elizabeth Bennet'
# }

# for keys, value in dictionary.items():
#    print(keys)

def test(d):
    # print( max(d, key=d.get))
    print( min(d, key=d.get))

students = {
    'Theodore': 19,
    'Roxanne': 22,
    'Mathew': 21,
    'Betty': 20
}
print(test(students))