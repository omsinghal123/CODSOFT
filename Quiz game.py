import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def check_answer(self, user_answer):
        if user_answer.lower() == self.questions[self.current_question]["answer"].lower():
            self.score += 1
        self.current_question += 1

        if self.current_question == len(self.questions):
            messagebox.showinfo("Quiz Game", f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}")
            root.destroy()
        else:
            self.display_question()

    def display_question(self):
        question_label.config(text=self.questions[self.current_question]["question"])
        option1.config(text=self.questions[self.current_question]["options"][0])
        option2.config(text=self.questions[self.current_question]["options"][1])
        option3.config(text=self.questions[self.current_question]["options"][2])
        option4.config(text=self.questions[self.current_question]["options"][3])

# Define the questions for the quiz
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Neptune", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Indira Gandhi", "Rajendra Prasad"],
        "answer": "Jawaharlal Nehru"
    },
    {
        "question": "When did India gain independence from British rule?",
        "options": ["1945", "1947", "1950", "1952"],
        "answer": "1947"
    },
    {
        "question": "Who was the leader of the Indian independence movement known as the Salt March?",
        "options": ["Mahatma Gandhi", "Subhash Chandra Bose", "Bhagat Singh", "Jawaharlal Nehru"],
        "answer": "Mahatma Gandhi"
    }
]

# Create an instance of the QuizGame
game = QuizGame(questions)

# Create the GUI using Tkinter
root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text="", font=("Arial", 12))
question_label.pack(pady=10)

option1 = tk.Button(root, text="", font=("Arial", 10), width=30, command=lambda: game.check_answer(option1.cget("text")), bg = "light blue")
option1.pack(pady=5)

option2 = tk.Button(root, text="", font=("Arial", 10), width=30, command=lambda: game.check_answer(option2.cget("text")), bg = "light blue")
option2.pack(pady=5)

option3 = tk.Button(root, text="", font=("Arial", 10), width=30, command=lambda: game.check_answer(option3.cget("text")), bg = "light blue")
option3.pack(pady=5)

option4 = tk.Button(root, text="", font=("Arial", 10), width=30, command=lambda: game.check_answer(option4.cget("text")), bg = "light blue")
option4.pack(pady=5)

# Start the quiz game
game.display_question()

# Run the main event loop
root.mainloop()