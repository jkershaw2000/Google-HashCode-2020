import logging as log
log.basicConfig(filename='./log.log', 
                level=log.INFO, 
                format='%(asctime)s %(message)s', 
                datefmt='%m/%d/%Y %I:%M:%S %p')

from operator import itemgetter


from classes.Library import Library
from classes.File import File
from classes.Book import Book



# Create libraries 
LIBRARIES = []

def main():
    data = File("../f_libraries_of_the_world.txt")
    log.info(data.wholeData)

    # Create libraries
    for lib in data.libraries:  
        
        l = Library(lib["days"], lib["numBooks"], lib["dailyScan"], lib["books"], lib["index"])
        LIBRARIES.append(l)

 
    # Creates list of max Score  for each library
    
    # maxScoreBooty = LIBRARIES.sort(key=lambda x: x.)
    maxScores = []
    for lib in LIBRARIES:
        maxScores.append([lib.maxTime(), lib])
        sorted(maxScores, key=itemgetter(0))
        
    
    log.info(maxScores)
    daysLeft = int(data.meta["days"])
    numberOfLibs = 0
    libIndexes = []
    books = []
    for key, value in enumerate(maxScores):
        if value[1].signUpTime < daysLeft:
            numberOfLibs += 1
            libIndexes.append(value[1].libraryID)
            daysLeft -= value[1].signUpTime
           # books[key] = value[1].books[:daily * daysLeft ]

            books.append(value[1].books)
   



    # Num of libs, libraries, books
    data.saveAnswer(numberOfLibs, libIndexes, books)
    
if __name__ == "__main__":
    log.info("Starting main...")
    main()


"""
    Time : Integer
    Books : Array of Books
    Libraries : Array of libraries

    Order Libraries by ScorePerDay
    Modify by Maxtime to minimise complete libraries

    "Simulate" to work which books are 

    SUBMIT
    Number of libraries - int
    Array of libs in order
    2D array of libs x books in order 
    
"""