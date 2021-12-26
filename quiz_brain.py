class QuizBrain:
    def __init__(self, questionList):
        self.questionNuMber = 0
        self.questionList = questionList

    def nextQuestion(self):
        question = self.questionList[self.questionNuMber]
        self.questionNuMber += 1
        input(f"Q.{self.questionNuMber}: {question.text} (True/False)?: ").lower()

    def stillHasQuestion(self):
        return self.questionNuMber < len(self.questionList)