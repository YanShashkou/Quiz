import question_model
import data
from quiz_brain import QuizBrain

question_bank = []
for question in data.question_data:
    question_bank.append(question_model.Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    print(len(quiz.questions_list))
    quiz.next_question()