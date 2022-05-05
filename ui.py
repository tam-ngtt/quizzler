from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=25, padx=25)

        # Score Label
        self.score_label = Label(text="Score: 0", font=("Arial", 13), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.text = self.canvas.create_text(150, 125, text=f"Text", font=("Arial", 20, "italic"),
                                            width=300, justify="center")

        # Buttons
        self.true_button = Button()
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button.config(image=self.true_image, borderwidth=0, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button()
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button.config(image=self.false_image, borderwidth=0, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.enable_buttons()
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"You've reached the end of the quiz."
                                                   f"\n\nYour final score is {self.quiz.score}.")
            self.disable_buttons()

    def is_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, result: bool):
        self.disable_buttons()
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

    def disable_buttons(self):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)

    def enable_buttons(self):
        self.true_button.config(state=ACTIVE)
        self.false_button.config(state=ACTIVE)