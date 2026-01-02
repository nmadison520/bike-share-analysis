import unittest
from exam_assignment import ExamAssignment 


class TestExam(unittest.TestCase):
    def setUP(self):
        exam = ExamAssignment("Project 3", "Sue Flay", 95, 75)
    def test_equal_same(self):
        self.AssertTrue(self.exam == self.exam)
    def test_equal_diff_type(self):
        self.AssertFalse(self.exam == "Sue Flay")
    def test_equal_same_tttt(self):
        temp = ExamAssignment("Project 3", "Sue Flay", 95.0, 75)
        self.AssertTrue(self.exam == temp)
    def test_equal_same_ttft(self):
        temp = ExamAssignment("Project 3", "Sue Flay", 95.1, 75)
        self.AssertFalse(self.exam == temp)
    if __name__ == '__main__':
        unittest.main()

    