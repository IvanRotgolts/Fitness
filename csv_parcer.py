from quiz import QuizItem

class QuizCSVParcer:
    """класс описывает csv_parcer"""

    def __init__(self, file_path, separator):
        self.file_path = file_path
        self.separator = separator
        self.items = []

    def parce_line(self, line):
         """делает разбор одной строкт"""
         columns = line.split(self.separator)
         question = columns[0]
         right_answer = columns[1]
         answers = columns[2:]

         return QuizItem(question = question, right_answer=right_answer, all_answers=answers)
    
    def parce_lines(self):
        """делает разбор целого файла и возвращает объекты QuizItem"""

        lines = []

        with open(self.file_path, "r", encoding = "utf-8") as file:
            lines=file.readlines()

        for line in lines:
            self.items.append(self.parce_line(line)) 

        return self.items
       