from modules._executor import Executor

app = Executor()
if __name__ == '__main__':
    
    # Leemos los archivos
    htmlData = app.readHtmlFolder(folderPath='html-files')
    
    
    # Escribimos el log con tiempos de lectura
    # app.writeLog(...)
    
    
    # Quitamos los tags de los datos: '<p>Hola</p>' -> 'Hola' 
    
    
    # Guardamos el log con tiempo que tardó en quitar tags
    # app.writeLog(...)


    # Separar palabras a una lista ejemplo 'hola mundo' -> ['hola', 'mundo']
    
    
    # Ordenar las palabras alfabeticamente
    
    