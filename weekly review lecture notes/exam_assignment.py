from assignment import Assignment

class ExamAssignment(Assignment):
    def __init__(self, title: str, student_name: str, score: float, time_limit=75):
        super().__init__(title, student_name, score)
        self.time_limit = time_limit

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is type(other):
            return (
                super().__eq__(other) and
                self.time_limit == other.time_limit
            )
        return NotImplemented

    def is_passed(self):
        return (self.score >= 70 and self.time_limit <= 75) or self.score >= 90