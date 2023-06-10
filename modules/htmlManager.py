import time
import re

class htmlManager:
    def __init__(self):
        pass
    
    

    def readHtmlFile(self, path):
        start_time = time.time()
        file = open(path, "r", errors="ignore")
        fileContents = file.read()
        fileName = file.name.split('/')[-1]
        ###

        ##PUNTO A) AQUI PUEDES BORRAR LAS ETIQUETAS DE FILE_CONTENTS, SEPARAR LAS PALABRAS, ETC.

        ###
        readTime = time.time() - start_time
        return {
            'fileName': fileName,
            'readTime': readTime,
            'fileContents': fileContents
        }
        
    
    def removeHtmlTags(self, content):
        # Reemplazamos los <br> con un espacio
        startTime = time.time()
        brReplacedWithSpace = re.sub(r'<br\s*/?>', ' ', content)
        contentNoTags = re.sub(r'<.*?>', '', brReplacedWithSpace, flags=re.DOTALL)
        endTime = time.time()
        return {
            'contentNoTags': contentNoTags,
            'removalTime': endTime-startTime
        }