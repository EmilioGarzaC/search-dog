import os 
from modules.htmlManager import htmlManager
from modules.txtManager import txtManager

class Executor:
    def __init__(self):
        self.htmlManager = htmlManager()
        self.txtManager = txtManager()
        pass
    
    

    def readHtmlFolder(self, folderPath):
        # Lista de archivos en folder
        htmlFiles = os.listdir(folderPath)
        print(htmlFiles)
        
        # Se ejecuta por cada archivo:
        #   self.htmlManager.readHtmlFile(fileName)
        
        pass
    