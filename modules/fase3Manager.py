import os
from modules.incidenciasOptMgr import incidenciasOptMgr
from modules.postingManager import postingManager

class fase3Manager:
    def __init__(self):
            self.incidenciasOptMgr = incidenciasOptMgr()
            self.postingManager = postingManager()
            pass

    def correr_fase_3(self):
        print("REPETICIONES: CUANTAS VECES APARECE EL TOKEN EN ESTE ARCHIVO")
        print("INCIDENCIAS: EN CUANTOS ARCHIVOS SALE EL TOKEN")
        root = os.path.dirname(os.path.abspath(__file__))
        output_files_path = os.path.join(root, "..", "output-files")
        path_alfabeticos = f"{output_files_path}\\ordenado_alfabetico"
        path_dataframe_completo = f"{output_files_path}\\dataframe_completo"
        path_posting_read = f"{output_files_path}\\posting\\posting.txt"
        path_diccionario = f"{output_files_path}\\diccionario\\diccionario.txt"
        path_indicador = f"{output_files_path}\\indicador\\indicador.txt"

        #Variables con los directorios que vamos a utilizar

        print("CREAR ARCHIVO POSTING")
        path_posting = f"{output_files_path}\\posting"
        #Crea el archivo de posting
        self.postingManager.generatePostingFile(f"{path_dataframe_completo}\\dataframe_completo.txt", path_alfabeticos, path_posting)

        #Crea el archivo diccionario (pendiente de arreglar)
        #createDataframe(path_posting_read, path_diccionario)
        #Crea el diccionario
        print("CREAR ARCHIVO INDICADOR")
        self.postingManager.crear_archivo_indicador(f"{path_dataframe_completo}\\dataframe_completo.txt", path_diccionario)
        print("CREAR HASHTABLE")
        #Crea la Hashtable y posteriormente ejecuta el metodo para escribir la hashtable en un archivo
        self.postingManager.createHashtable(path_diccionario, f"{output_files_path}\\hashtable_ascii\\hashtable.txt")
        #Limpia el dccionario 
        print("LIMPIAR DICCIONARIO")
        self.postingManager.limpiarDiccionario()
        #Reemplaza la columna pesos archivo
        print("AGREGAR PESOS A POSTING")
        path_pesos = f"{output_files_path}\\pesos\\pesos.txt"
        self.postingManager.reemplazar_columna_pesos_archivo(path_posting_read, path_pesos)
        print("FASE 3 END")