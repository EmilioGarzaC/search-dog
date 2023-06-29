import os
import pickle
from hashtable import HashTable
import pandas as pd
import csv

class postingManager:
    def __init__(self):
        pass
    #ACTIVIDAD 7 PARTE 1
        # Una función que haga un nuevo dataframe que va a ser el archivo de posting. 
        # En este dataframe, por cada token de la dataframe H11, va a buscar en que 
        # documento aparece ese token, y las repeticiones de esa palabra en el documento, 
        # y va a agregar estas al dataframe nuevo. Al final esto se guarda como un archivo nuevo.
    def generatePostingFile(self, source_path, data_path, output_path):
            h11_df= pd.read_csv(source_path)
            posting_df = pd.DataFrame({"DOCUMENTO":[],
                                    "REPETICIONES":[]})
            for index, row in h11_df.iterrows():
                token = row['TOKEN']
                folderFiles = os.listdir(data_path)
                for file in folderFiles:
                        alpha_df= pd.read_csv(f'{data_path}/{file}')
                        if token in alpha_df["TOKEN"].values:
                            repeticiones = alpha_df[alpha_df.TOKEN==token].REPETICIONES.item()
                            new_col = pd.DataFrame({"DOCUMENTO":[file.replace("_modificado_frecuencias.txt", ".html")],
                                                    "REPETICIONES":[repeticiones]})
                            posting_df = posting_df._append(new_col, ignore_index = True)
            print(posting_df)
            with open(f'{output_path}\\posting.txt', 'w') as new_file:
                new_file.write(posting_df.to_csv(index=False))
            pass

    #ACTIVIDAD 7 PARTE 2 (Pendiente por arreglar)
    #entrada = posting.txt
    #salida = diccionario.txt

    #ACTIVIDAD 7 PARTE 2
    def crear_archivo_indicador(self, archivo_entrada, archivo_salida):
            # Read the file and create a DataFrame
            h11_df = pd.read_csv(archivo_entrada)  # Replace 'input_file.csv' with your file path and name
            ubicaciones = []
            i = 0
            for index, row in h11_df.iterrows():
                ubicaciones.append(i)
                i += row['INCIDENCIAS']
            h11_df = self.agregar_columna(h11_df, "UBICACION", ubicaciones)
            h11_df = h11_df.drop('INCIDENCIAS', axis=1)
            # Output datatable to diccionario.txt file
            with open(archivo_salida, 'w') as new_file:
                h11_df = h11_df.to_csv(sep=';', index=False, header=False)
                h11_df = h11_df.replace('\n', '')
                new_file.write(h11_df)
            pass
            print("Datos ordenados y guardados en el archivo:", archivo_salida)


    #ACTIVIDAD 8 PARTE 2 
    # dictionary file = diccionario.txt
    # Crea la hashtable en base a el archivo diccionario y ejecuta el metodo para imprimir la hashtable en un archivo
    def createHashtable(self, dictionaryFile, path_ascii_output):

        # Leemos archivo diccionario
        with open(dictionaryFile) as f:
                lines = f.readlines()
                
        # Creamos tabla hash con espacio de 40 como mínimo
                tablaHash = HashTable(round(len(lines)*1.2) if len(lines) > 50 else 40)
                
        # Leemos las lineas del archivo e insertamos los valores a tabla hash
        for line in lines:
                    splitLine = line.split(';')
                    tablaHash[splitLine[0]] = [splitLine[1], splitLine[2]]


        # Definimos spacing para el archivo (40 espacios, 8 ..., 8 ...)
        delim = "%40s%8s%8s"

        # Generamos el contenido para el archivo en base a la tabla hash
        contenidoTxtHash = '\n'.join([delim % (hashRow[0][0], hashRow[0][1][0], hashRow[0][1][1]) if hashRow != None else delim % ('', 0, -1) for hashRow in tablaHash.data])

        self.write_hashtable_to_ascii_file(contenidoTxtHash, path_ascii_output)


    #ACTIVIDAD 8 PARTE 3
    #Escribe la hashtable que recibe como parametro en un archivo

    def write_hashtable_to_ascii_file(self, hashtable, filepath):
        with open(filepath, "wb") as file:
            # Serialize and write the hashtable object to the file
            pickle.dump(hashtable, file)

        print("Hashtable written to file successfully.")

    #Actividad 9
    def limpiarDiccionario(self):
        root = os.path.dirname(os.path.abspath(__file__))
        output_files_path = os.path.join(root, "..", "output-files")
        dfStop = pd.read_csv(f"{output_files_path}\\stop-list.txt",  header=None)
        dfDic = pd.read_csv(f"{output_files_path}\\diccionario\\diccionario.txt", sep=';', names=['TOKEN', 'REPETICIONES', 'UBICACION'])
        print(dfDic)
        #if 1 in dfDic.columns:
        for index, row in dfDic.iterrows():
            # If the word is found in the stop list
            if row[0] in set(dfStop[0]):
                dfDic = dfDic.drop(index)
                
            # If the word repetitions are less than 5
            elif row[1] < 5:
                dfDic = dfDic.drop(index)
                
            # If the word has a length of 1
            elif len(row[0]) == 1:
                dfDic = dfDic.drop(index)
            
        with open(f'{output_files_path}\\limpio\\limpio.txt', 'w') as new_file:
            new_file.write(dfDic.to_csv(index=False))
        pass
        #else:
        #    print("Column index 1 does not exist in the DataFrame dfDic.")

    #ACTIVIDAD 10 
    def reemplazar_columna_pesos_archivo(self, archivo_repeticiones, archivo_salida):
            with open(archivo_repeticiones, 'r') as file:
                posting = pd.read_csv(file)
                pesos = []

            for index, row in posting.iterrows():
                repeticiones = row['REPETICIONES']
                total_tokens = self.contar_tokens(row["DOCUMENTO"])
                peso = repeticiones * 100 / total_tokens  # Función para calcular el peso basado en las repeticiones
                pesos.append(peso)
            
            posting = self.agregar_columna(posting, 'PESO', pesos)
            posting = posting.drop('REPETICIONES', axis=1)     
            with open(archivo_salida, 'w') as new_file:
                new_file.write(posting.to_csv(index=False))
            pass

    def contar_tokens(self, archivo):
            root = os.path.dirname(os.path.abspath(__file__))
            output_files_path = os.path.join(root, "..", "output-files")
            ruta_archivo = f"{output_files_path}\\split-words\\{archivo}"
            ruta_archivo = ruta_archivo.replace(".html", ".txt")
            with open(ruta_archivo, 'r') as archivo_origen:
                contenido = archivo_origen.read()
                tokens = contenido.split()
                return(len(tokens))        

    def agregar_columna(self, dataframe, nombre_columna, valores):
            dataframe[nombre_columna] = valores
            return dataframe