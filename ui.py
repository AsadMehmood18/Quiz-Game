from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window= Tk()
        self.window.title ("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR,fg="white",highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        self.space = Canvas(width=300, height=250, bg="white")
        self.question_text=self.space.create_text(150, 125, width=280, text="PlaceHolder Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.space.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR, command=self.correct_answer)
        self.true_button.grid(row=2, column=0)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR, command=self.wrong_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.space.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.space.itemconfig(self.question_text, text=q_text)
        else:
            self.space.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.space.config(bg="green")
        else:
            self.space.config(bg="red")
        self.window.after(1000, self.get_next_question)

