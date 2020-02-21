import sys
sys.path.append("..")
from classes.Book import Book

class Library():
    """
    signUpTime  - Days the library takes to make
    numBooks    - Number of books contained
    dailyScan   - Number of books that can be scanned per day
    books       - Array of books 
    """
    def __init__(self, signUpTime, numBooks, dailyScan, books, libraryID):
        self.libraryID = libraryID
        self.signUpTime = int(signUpTime)
        self.numBooks = int(numBooks)
        self.dailyScan = int(dailyScan)       
        self.books = []
        books.sort()
        for book in books:
            self.books.append(Book(int(book)))

       

    def __str__(self):
        return ("Sign up Time: %d\nNumber of Books: %d\nDaily Scan: %d\nLibrary ID: %d" %(self.signUpTime, self.numBooks, self.dailyScan, self.libraryID))


    def maxTime(self):
        """The max days that the library can be used for"""
        return self.signUpTime + self.numBooks / self.dailyScan
        
    def maxScore(self, days):
        """If ran from day 1, maximun score this library could produce"""
        maxBooksProcessed = self.dailyScan * (int(days) - int(self.signUpTime))
        print(self.books)
        return sum([x.score for x in self.books[0:maxBooksProcessed]])
        
    def maxScorePerDay(self, daysToRun):
        """Average score per day with daysToRun remaing when sign up begins"""
        scanningDays = daysToRun - self.signUpTime
        maxScore = sum([x.score for x in self.books[:(2*scanningDays)]])
        return maxScore / daysToRun



"""
    Maxtime: Number of days it takes to setup + process all books
    MaxScore: Maximum score the library can give
    ScorePerDay: Score per day running
"""
    

    
    