import os
import math
from modules.incidenciasOptMgr import incidenciasOptMgr
from modules.postingManager import postingManager
import pandas as pd

class fase4Manager:
    def __init__(self):
            self.incidenciasOptMgr = incidenciasOptMgr()
            self.postingManager = postingManager()
            pass
    
    #ACTIVIDAD 11
    def indexar_archivos(self, path_pesos, path_index, path_posting_index): 
        #PARAMETROS: archivo de peso y directorio de index_documento      
        #crea un archivo de index_documento que contiene el id para cada documento
        posting = pd.read_csv(path_pesos)
        index_documento = pd.DataFrame({"ID":[], "DOCUMENTO":[]})
        posting_indexado = pd.DataFrame({"ID":[], "PESO":[]})
        for index, row in posting.iterrows():
            document = row['DOCUMENTO']
            peso = row['PESO']
            i = str(index)
            new_col = pd.DataFrame({"ID":[i], "DOCUMENTO":[document]})
            index_documento = index_documento._append(new_col, ignore_index = True)
            new_col = pd.DataFrame({"ID":[i], "PESO":[peso]})
            posting_indexado = posting_indexado._append(new_col, ignore_index = True)

        #index_documento
        with open(path_index, 'w') as new_file:
            new_file.write(index_documento.to_csv(index=False))
        pass
        #posting_indexado
        with open(path_posting_index, 'w') as new_file:
            new_file.write(posting_indexado.to_csv(index=False))
        pass         

    #ACTIVIDAD 12
    def search(self, path_diccionario, path_documentos):
        #Indica al usuario escribir la palabra a buscar
        palabra = input("Escribe la palabra a buscar: ")
        #La palabra se cambia a minúsculas en caso de que no sea así
        palabra = palabra.lower()
        results = []
        df_diccionario = pd.read_csv(path_diccionario, sep=';', names=["TOKEN", "REPETICIONES", "UBICACION"])
        if palabra in df_diccionario["TOKEN"].values:
            dict_index = df_diccionario[df_diccionario['TOKEN'] == palabra].index
            row_start = df_diccionario.iloc[dict_index]
            row_end = df_diccionario.iloc[dict_index+1]
            p_index_start = row_start['UBICACION'].values[0]
            p_index_end = row_end['UBICACION'].values[0]
            df_documentos = pd.read_csv(path_documentos)
            for i in range(p_index_start, p_index_end):
                doc_row = df_documentos.loc[df_documentos['ID'] == i]
                doc_name = doc_row["DOCUMENTO"].values[0]
                results.append(doc_name)
            print("RESULTADOS DE BUSQUEDA")
            print(results)
            
            return {
                'documentos': results,
                'p_start': p_index_start,
                'p_end': p_index_end,
            }
        else:
            print(f"{palabra} no existe en el diccionario")
            return False
    
     #Actividad 12
    def limpiarDiccionario(self, path_stoplist, path_diccionario, path_output):
        dfStop = pd.read_csv(path_stoplist,  header=None)
        dfDic = pd.read_csv(path_diccionario, sep=';', names=['TOKEN', 'REPETICIONES', 'UBICACION'])
        #print(dfDic)
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
            
        with open(path_output, 'w') as new_file:
            new_file.write(dfDic.to_csv(index=False))
        pass
        #else:
        #    print("Column index 1 does not exist in the DataFrame dfDic.")


    #ACTIVIDAD 13
    def filtrar_por_peso(self, act12, path_pesos):
        pesos = pd.read_csv(path_pesos)
        p_start = act12["p_start"]
        p_end = act12["p_end"]
        pesos = pesos[p_start:p_end]
        ordenados = pesos.sort_values(by='PESO', ascending=False)
        ordenados = ordenados[0:9]
        print("ORDENADOS")
        print(ordenados)

    def correr_fase_4(self):
        print("Fase 4")
        root = os.path.dirname(os.path.abspath(__file__))
        output_files_path = os.path.join(root, "..", "output-files")
        path_pesos = f"{output_files_path}\\pesos\\pesos.txt"
        path_index = f"{output_files_path}\\index_documents\\index_documents.txt"
        path_diccionario = f"{output_files_path}\\diccionario"
        #Variables con los directorios que vamos a utilizar
        print("ACTIVIDAD 11")
        print("INDEX DOCUMENTS")
        #self.indexar_archivos(path_pesos, path_index, path_posting_index)
        print("ACT 12: LIMPIAR DICCIONARIO")
        #self.limpiarDiccionario(path_stoplist, f"{path_diccionario}\\diccionario.txt", f"{path_diccionario}\\diccionarioLimpio.txt")
        #Gauch, elephants, CSCE , Arkansas, gift, abcdef, 20, 20.07, 123-456-7890, lawyer consumers, garden computer, United States laws
        while True:
            print("ACTIVIDAD 12: BUSCAR PALABRAS")
            act12 = self.search(f"{path_diccionario}\\diccionario.txt", path_index)
            if act12 != False:
                print("ACTIVIDAD 13: TOP 10")
                self.filtrar_por_peso(act12, path_pesos)
            opt = input("Continuar? Ingresa N para salir.")
            if opt == "N":
                break

        print("FASE 4 TERMINADA")