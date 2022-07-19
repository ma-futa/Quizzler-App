from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, )

        self.score_label = Label(text=f'Score: 0', font=('Arial', 20, 'bold'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg='white', height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.question = 'food food food'
        self.canvas_text = self.canvas.create_text(150, 125, width=280, fill=THEME_COLOR, text=self.question)

        right_img = PhotoImage(file='./images/true.gif')
        self.right_button = Button(command=self.yes, image=right_img, highlightbackground=THEME_COLOR,
                                   highlightcolor=THEME_COLOR, highlightthickness=0, borderwidth=0)
        self.right_button.grid(row=2, column=0, padx=20)

        wrong_img = PhotoImage(file='./images/false.gif')
        self.wrong_button = Button(command=self.no, image=wrong_img, highlightbackground=THEME_COLOR,
                                   highlightcolor=THEME_COLOR, highlightthickness=0, borderwidth=0)
        self.wrong_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text,fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.canvas_text, text="youve reached the end of this Quiz", fill=THEME_COLOR)
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def yes(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def no(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right: bool):
        self.canvas.itemconfig(self.canvas_text, fill='white')
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
