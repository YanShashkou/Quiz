class QuizBrain:
    def __init__(self,questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        answer = input(f'Q.{self.question_number + 1},{self.questions_list[self.question_number].text}, please enter your answer (True/False)')
        self.question_number += 1
        self.check_answer(answer, self.questions_list[self.question_number].answer)


    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


    def check_answer(self,answer,correct_answer):
        if answer == correct_answer:
            print('Correct!')
            self.score +=1
        else:
            print('Incorrect!')
            print(f"The correct answer is {correct_answer}")
            print(f"Your score is {self.score}/{self.question_number}")

