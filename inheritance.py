class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        score_count = len(scores)
        score_sum = sum(scores)
        avg_score = int(score_sum)//int(score_count)

        if 90<= avg_score <= 100: return 'O'
        elif 80<= avg_score < 90: return 'E'
        elif 70<= avg_score < 80: return 'A'
        elif 55<= avg_score < 70: return 'P'
        elif 40<= avg_score < 55: return 'D'
        else: return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNumber = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNumber, scores)
s.printPerson()
print("Grade:", s.calculate())