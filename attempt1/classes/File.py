import logging as log
log.basicConfig(filename='./log.log', 
                level=log.INFO, 
                format='%(asctime)s %(message)s', 
                datefmt='%m/%d/%Y %I:%M:%S %p')

import os

class File():
    def __init__(self, filepath):

        with open(filepath, "r") as f:
            data = [x.replace("\n", "") for x in f.readlines()]

            self.meta = data[0].split(" ")
            self.meta = {
                "numBooks": self.meta[0],
                "libs": self.meta[1],
                "days": self.meta[2]
            }
            self.bookScores = data[1].split(" ")

            data.pop(0)
            data.pop(0)
            libs = [x for x in range(0,len(data), 2)]
            books = [x for x in range(1,len(data), 2)]
            self.libraries = [{"numBooks": data[libs[key]].split(" ")[0], "days": data[libs[key]].split(" ")[1], "dailyScan": data[libs[key]].split(" ")[2], "index": key, "books": data[value].split(" ")} for key, value in enumerate(books)]

            log.info(self.meta)
            log.info(self.bookScores)
            log.info(self.libraries)

            self.wholeData = {
                "meta": self.meta,
                "bookScores": self.bookScores,
                "libs": self.libraries
            }

    def saveAnswer(self, numOfLibraries, libraries, books):
        """
            Save answer to new file

            @param numObLibraries - INT of the amount of libraries used
            @param libraries - 1d array of the library IDs used
            @param books - 2d array ordered in the order of the libraries used
        """

        cpt = sum([len(files) for r, d, files in os.walk("./submissions")])
        filepath = "./submissions/Submission"+str(cpt+1)+".txt"
        with open(filepath, "w+") as f:
            f.write(str(numOfLibraries)+"\n")
            
            for lib in range(len(libraries)):
                b = list(dict.fromkeys(books[lib]))
                b2 = []
                for x in b:
                    if str(x.score) not in b2: 
                        b2.append(str(x.score))
                
                f.write(str(libraries[lib])+" "+str(len(b2))+"\n")
                f.write(" ".join(b2)+"\n")
            
            log.info("Answer saves to.."+filepath)


    