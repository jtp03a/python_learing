from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []

questions = question_data['results']

for question in questions:
  new_question = Question(html.unescape(question["question"]), question["correct_answer"])
  question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
  quiz_brain.next_question()

quiz_brain.score_report()
