import numpy as np


# class for multiplication problems
class myMultiplicationProblems():
    """
    This class creates multiplication problems.
    It is also the base class for other types of problems.
    """
    def __init__(self):
        self.num1 = np.random.randint(10)
        self.num2 = np.random.randint(10)
        self.operation = "multiply"
        self.operationSign = "X"
        self.correctAnswer = self.num1 * self.num2
        self.time_to_response = 0
        self.players_response = ""
        self.custom_class_functions()
        self.isCorrect = "Incorrect answers"

    def custom_class_functions(self):
        pass

# class for addition problems
class myAdditionProblems(myMultiplicationProblems):
    def custom_class_functions(self):
        """
        All problems are initially created as multiplication problems.
        This method customises the problems, depending on class.
        """
        self.operation = "add"
        self.operationSign = "+"
        self.correctAnswer = self.num1 + self.num2


# class for subtraction problem
class mySubtractionProblems(myMultiplicationProblems):
    def custom_class_functions(self):
        self.operation = "subtract"
        self.operationSign = "-"
        self.correctAnswer = self.num1 - self.num2

class exitGame(Exception):
    def __init__(self, message):
        print(f"Well: {message}")
        super().__init__(message)
        exit(0)

