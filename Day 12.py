# Inheritance in python3

# person = base class
# student = derived class
# write a student class constructor with 4 parameters :
# first name
# last name
# idNumber
# array of test scores
# a calculate method to print average grade of the student
'''
# Hackerrank implements them on their own .....
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
'''
class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,fname,lname,id,scr):
        self.firstName = fname
        self.lastName = lname
        self.idNumber = id
        self.scores = scr
    #   Function Name: calculate
    def calculate(self):
    #   Return: A character denoting the grade.
        avg = sum(self.scores)/len(self.scores)
        if avg >= 90 : return 'O'
        elif avg >= 80 : return 'E'
        elif avg >= 70 :return 'A'
        elif avg >= 55 :return 'P'
        elif avg >= 40 :return 'D'
        else:return 'T'
'''
if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
'''
