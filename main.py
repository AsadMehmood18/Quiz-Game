from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

question_bank = []
for dat in question_data:
    new_q = dat["question"]
    new_a = dat["correct_answer"]
    question_bank.append(Question(new_q, new_a))
print(len(question_bank))
quiz=QuizBrain(question_bank)
print(logo)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

