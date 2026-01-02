from abc import ABC, abstractmethod

class Assignment(ABC):
    def __init__(self, title: str, student_name: str, score: float):
        self.title = title
        self.student_name = student_name
        self.score = score
    
    def __str__(self):
        return f"{self.title}\n{self.student_name}\{self.score}"
    
    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return NotImplemented
        return (
            self.title == other.title and
            self.student_name == other.student_name and
            abs(self.score - other.score) < 0.000001
        )
    #@abstractmethod tag, is not a keyword
    @abstractmethod
    def is_passed(self):
        pass