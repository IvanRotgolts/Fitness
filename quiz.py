class QuizItem:
    """класс описвает объект викторины"""

    def __init__(self, question, right_answer, all_answers) -> None:
        self.question = question
        self.right_answer = right_answer
        self.all_answers = all_answers

    def get_question(self):
        return self.question
    
    def get_right_answer(self):
        return self.right_answer
    
    def get_answers(self):
        return self.all_answers