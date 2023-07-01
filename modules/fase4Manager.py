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


    def correr_fase_4(self):
        print("Fase 4")
        root = os.path.dirname(os.path.abspath(__file__))
        output_files_path = os.path.join(root, "..", "output-files")
        path_pesos = f"{output_files_path}\\pesos\\pesos.txt"
        path_index = f"{output_files_path}\\index_documents\\index_documents.txt"
        path_posting_index = f"{output_files_path}\\index_posting\\index_posting.txt"
        path_alfabeticos = f"{output_files_path}\\ordenado_alfabetico"
        path_dataframe_completo = f"{output_files_path}\\dataframe_completo"
        path_posting_read = f"{output_files_path}\\posting\\posting.txt"
        path_diccionario = f"{output_files_path}\\diccionario\\diccionario.txt"
        path_indicador = f"{output_files_path}\\indicador\\indicador.txt"

        #Variables con los directorios que vamos a utilizar
        print("ACTIVIDAD 11")
        print("INDEX DOCUMENTS")
        self.indexar_archivos(path_pesos, path_index, path_posting_index)
        self.postingManager.limpiarDiccionario()
        print("FASE 4 TERMINADA")