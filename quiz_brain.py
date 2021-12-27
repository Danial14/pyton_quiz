class QuizBrain:
    def __init__(self, questionList):
        self.questionNuMber = 0
        self.questionList = questionList
        self.score = 0

    def nextQuestion(self):
        question = self.questionList[self.questionNuMber]
        self.questionNuMber += 1
        userAnswer = input(f"Q.{self.questionNuMber}: {question.text} (True/False)?: ").lower()
        self.checkAnswer(userAnswer, question.answer.lower())

    def stillHasQuestion(self):
        return self.questionNuMber < len(self.questionList)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer == correctAnswer:
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {correctAnswer}")
        print(f"Your current score is: {self.score} / {self.questionNuMber}")
        print("\n")