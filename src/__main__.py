from modules._executor import Executor
import time 

app = Executor()
if __name__ == '__main__':
    
    # Actividad 1 ========================================================
    
    # Registramos tiempo de inicio
    startRead = time.time()
    
    # Leemos los archivos
    htmlData = app.readHtmlFolder(folderPath='html-files')
    
    # Escribimos el log con tiempos de lectura
    readTimesData = [[fileName, data['readTime']] for fileName, data in htmlData.items()]
    totalReadTime = sum([data['readTime'] for fileName, data in htmlData.items()])
    readTimesString = '\n'.join([f"{readData[0]}, {readData[1]}" for readData in readTimesData])

    endRead = time.time()
    app.writeLog(
        fileName= 'a1_2725177',
        title= 'FILE READ TIMES',
        body= readTimesString,
        footer= f'\nTotal read time: {totalReadTime}\nTotal execution time: {endRead-startRead}'
    )
    
    
    
    # Actividad 2 ========================================================
    
    # Registramos tiempo de inicio
    startRemoval = time.time()
    
    # Quitamos los tags de los datos 
    htmlDataNoTags = app.removeHtmlTags(htmlData)
    
    # Escribimos el log con tiempos de removal
    removalTimesData = [[fileName, data['removalTime']] for fileName, data in htmlDataNoTags.items()]
    totalRemovalTime = sum([data['removalTime'] for fileName, data in htmlDataNoTags.items()])
    removalTimesString = '\n'.join([f"{removalData[0]}, {removalData[1]}" for removalData in removalTimesData])
    
    endRemoval = time.time()
    app.writeLog(
        fileName= 'a2_2725177',
        title= 'TAG REMOVAL TIMES',
        body= removalTimesString,
        footer= f'\nTotal removal time: {totalRemovalTime}\nTotal execution time: {endRemoval-startRemoval}'
    )
    

    # Actividad 3 ========================================================
    
    # Registramos tiempo de inicio
    startSplitSort = time.time()
    
    # Separar palabras a una lista y ordenarlas
    htmlDataSplitSorted = app.splitContentIntoOrderedList(htmlDataNoTags)
    
    # Escribimos el log con tiempos de removal
    splitOrderTimesData = [[fileName, data['splitTime'] + data['orderTime']] for fileName, data in htmlDataSplitSorted.items()]
    totalSplitOrderTime = sum([data['splitTime'] + data['orderTime'] for fileName, data in htmlDataSplitSorted.items()])
    splitOrderTimesString = '\n'.join([f"{splitOrderData[0]}, {splitOrderData[1]}" for splitOrderData in splitOrderTimesData])
    
    endSplitSort = time.time()
    app.writeLog(
        fileName= 'a3_2725177',
        title= 'WORD SPLITTING AND SORTING TIMES',
        body= readTimesString,
        footer= f'\nTotal split & sorting time: {totalSplitOrderTime}\nTotal execution time: {endSplitSort-startSplitSort}'
    )
    
    # Escribimos las palabras ordenadas a un txt
    for fileName, data in htmlDataSplitSorted.items():
        cleanWordList = data['contentSplitOrdered']
        txtContent = '\n'.join([string for string in cleanWordList])
        app.writeToTxt('split-words', fileName.replace('.html', ''), content=txtContent)
    

    # FASE 2
    app.runFase2()