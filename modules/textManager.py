import time
import string
import re

class textManager:
    def __init__(self):
        pass
    
    
    
    def writeToTxt(self, path, fileName, text):
        filePath = path + "/" + fileName + ".txt"
        with open(filePath, "w") as file:
            file.write(text)
    
    
    def splitText(self, text):
        startTime = time.time()
        listOfStrings = text.split()
        endTime = time.time()
        return {
            'splitContentList': listOfStrings,
            'splitTime': endTime-startTime
        }

      
    # Move pending
    def orderList(self, wordList):
        startTime = time.time()
        orderedList = sorted(wordList, key=str.lower)
        endTime = time.time()
        return {
            'orderedList': orderedList,
            'orderTime': endTime-startTime
        }

    def filterTrash(self, listToCleanse):
        cleanWords = []
        for word in listToCleanse:
            email_pattern = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
            url_pattern = r'^(http|https)://[^\s/$.?#].[^\s]*$'

            if re.match(email_pattern, word) or re.match(url_pattern, word):
                continue
            
            wordNoPunc = word.translate(str.maketrans('', '', string.punctuation))
            if wordNoPunc.isalpha():
                cleanWords.append(wordNoPunc)
        
        return cleanWords
    