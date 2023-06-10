import os
import time
from modules.htmlManager import htmlManager
from modules.textManager import textManager

class Executor:
    def __init__(self):
        self.htmlMgr = htmlManager()
        self.txtMgr = textManager()
        pass
    
    

    def readHtmlFolder(self, folderPath):
        htmlData = {}
        fileList = os.listdir(folderPath)
        
        for fileName in fileList:
            fileData = self.htmlMgr.readHtmlFile(f"{folderPath}/{fileName}")
            htmlData[fileData['fileName']] = {'content':fileData['fileContents'], 'readTime':fileData['readTime']}
            
        return htmlData
    
    
    def removeHtmlTags(self, htmlData):
        htmlFileContentsNoTags = {}
        for fileName, fileData in htmlData.items():
            content = fileData['content']

            dataNoTags = self.htmlMgr.removeHtmlTags(content)

            htmlFileContentsNoTags[fileName] = {
                'content': fileData['content'],
                'contentNoTags': dataNoTags['contentNoTags'],
                'readTime': fileData['readTime'],
                'removalTime': dataNoTags['removalTime']
            }

        return htmlFileContentsNoTags
           
    
    def splitContentIntoOrderedList(self, htmlData):
        htmlFileContentsSplit= {}
        for fileName, fileData in htmlData.items():
            contentToSplit = fileData['contentNoTags']
            
            contentSplitData = self.txtMgr.splitText(contentToSplit)
            cleanWordsList = self.txtMgr.filterTrash(contentSplitData['splitContentList'])
            contentSplitOrderedData = self.txtMgr.orderList(cleanWordsList)
            
            htmlFileContentsSplit[fileName] = {
                'content': fileData['content'],
                'contentNoTags': fileData['contentNoTags'],
                'contentSplit': contentSplitData['splitContentList'],
                'contentSplitOrdered': contentSplitOrderedData['orderedList'],
                'readTime': fileData['readTime'],
                'removalTime': fileData['removalTime'],
                'splitTime': contentSplitData['splitTime'],
                'orderTime': contentSplitOrderedData['orderTime']
            }
            
        return htmlFileContentsSplit
    
    
    def writeLog(self, fileName, title, body, footer):
        logText = f"############# {title} #############\n{body}\n{footer}"
        self.txtMgr.writeToTxt(path='log-files', fileName=fileName, text=logText)
    
    
    def writeToTxt(self, path, fileName, content):
        self.txtMgr.writeToTxt(path=f'output-files/{path}', fileName=fileName, text=content)
    
        
    def purgeNonWords(self, listToCleanse):
        cleanWordsList = self.txtMgr.filterTrash(listToCleanse)
        return cleanWordsList