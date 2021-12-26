from data import question_data
import question_model
import quiz_brain
questionBank = []
for data in question_data:
    question = question_model.Question(data["text"], data["answer"])
    questionBank.append(question)

quiz = quiz_brain.QuizBrain(questionBank)
while quiz.stillHasQuestion():
    quiz.nextQuestion()