class QuizBrain:
  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0

  def still_has_questions(self):
    return len(self.question_list) > self.question_number

  def check_answer(self, correct_answer, user_answer):
    return correct_answer.lower() == user_answer.lower()

  def score_report(self):
    print(self.score)

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    if self.check_answer(current_question.answer, user_answer):
      print("Correct")
      self.score += 1
    else:
      print("Incorrect")
