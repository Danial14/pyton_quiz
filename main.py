from data import question_data
import question_model
import quiz_brain
questionBank = []
for data in question_data:
    question = question_model.Question(data["question"], data["correct_answer"])
    questionBank.append(question)

quiz = quiz_brain.QuizBrain(questionBank)
while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("You have coMpleted the quiz")
print(f"Your final score was: {quiz.score} / {quiz.questionNuMber}")