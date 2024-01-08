from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_text = data["text"]
    question_answer = data["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

final_score = quiz.final_score()
#also quiz.score will return the final score 


print("You've completed the quiz")
print(f"Your final score was: {final_score}/{quiz.question_number}")
