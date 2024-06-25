import unittest
from celebral_logic import *
from celebral_classes import *


class TestCelebralClasses(unittest.TestCase):
    def test_myMultiplicationProblems(self):
        problem = myMultiplicationProblems()
        self.assertIsInstance(problem, myMultiplicationProblems)

    def test_myAdditionProblems(self):
        problem = myAdditionProblems()
        self.assertIsInstance(problem, myAdditionProblems)

    def test_mySubtractionProblems(self):
        problem = mySubtractionProblems()
        self.assertIsInstance(problem, mySubtractionProblems)

class TestGenerateProblems(unittest.TestCase):
    def test_generate_problems(self):
        problems = generate_problems()
        self.assertEqual(len(problems), 9)

class TestSolveProblems(unittest.TestCase):
    def test_solve_problems(self):
        problem = myMultiplicationProblems()
        solved = solve_problem(problem, problem.correctAnswer)
        self.assertIsInstance(solved, myMultiplicationProblems )

class TestCreateDataFrame(unittest.TestCase):
    def test_create_dataframe(self):
        problems = generate_problems()
        df = create_dataframe(problems)
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
