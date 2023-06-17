import os
from collections import Counter
import glob
import pandas as pd
from modules.incidenciasOptMgr import incidenciasOptMgr

class fase2Manager:
    def __init__(self):
        self.incidenciasOptMgr = incidenciasOptMgr()
        pass

    #HISTORIA H7
    def convertirMinusculas(self, directorio, output_path):
        archivos = glob.glob(os.path.join(directorio, '*'))
        archivos_txt = [archivo for archivo in archivos if archivo.endswith('.txt')]
        for archivo in archivos_txt:
            tokens = []
            file = open(archivo, "r")
            for line in file:
                line = line.strip()
                line = line.lower()
                tokens.append(line)
            tokens.sort()
            contenido_modificado = '\n'.join(tokens)
            nuevo_nombre = (os.path.basename(archivo))
            nuevo_nombre = nuevo_nombre.replace('.txt', '_modificado.txt')
            with open(f'{output_path}\\{nuevo_nombre}', 'w') as new_file:
                new_file.write(contenido_modificado)

    # HISTORIA H9
    def generar_archivos_frecuencia_alfabetica(self, origen, destino):
        archivos = os.listdir(origen)
        print(archivos)
        for archivo in archivos:
            ruta_archivo = os.path.join(origen, archivo)
    
            if os.path.isfile(ruta_archivo):
                with open(ruta_archivo, 'r') as archivo_origen:
                    contenido = archivo_origen.read()
                    palabras_archivo = contenido.split()
    
                    frecuencia_palabras = Counter(palabras_archivo)
                nombre_archivo = archivo.split('.')[0] + '_frecuencias.txt'
                ruta_destino = os.path.join(destino, nombre_archivo)
                data_frame = pd.DataFrame(frecuencia_palabras.items(), columns=['TOKEN', 'REPETICIONES'])
                data_frame.to_csv(ruta_destino, index=False, sep=',')
    
    # HISTORIA H10
    def generar_archivos_repeticiones(self, frequenciesFolder, output_path):
        aggregatedFrequencies = {}
        
        folderFiles = os.listdir(frequenciesFolder)
        for file in folderFiles:
            with open(f'{frequenciesFolder}/{file}') as f:
                lines = f.readlines()[1:] # Skips header
                for line in lines:
                    word, frequency = line.split(',')
                    if word in aggregatedFrequencies.keys():
                        aggregatedFrequencies[word] = int(frequency) + aggregatedFrequencies[word]
                    else:
                        aggregatedFrequencies[word] = int(frequency)
                        
        #converts to csv
        sortedFrequencies = sorted(aggregatedFrequencies.items(), key=lambda x:x[1], reverse=True)
        fileBody = '\n'.join([f'{freq[0]}, {freq[1]}' for freq in sortedFrequencies])
        #saves to file as dataframe
        with open(f'{output_path}\\repeticiones.txt', 'w') as new_file:
            new_file.write(f"TOKEN, REPETICIONES\n{fileBody}")
        pass
        # app.writeToTxt(path=frequenciesFolder, fileName='aggregated_frequencies', text=fileBody)

     # LLAMADAS
    def correr_fase_2(self):
        print("REPETICIONES: CUANTAS VECES APARECE EL TOKEN EN ESTE ARCHIVO")
        print("INCIDENCIAS: EN CUANTOS ARCHIVOS SALE EL TOKEN")
        root = os.path.dirname(os.path.abspath(__file__))
        output_files_path = os.path.join(root, "..", "output-files")
        path_split_words = f"{output_files_path}\\split-words"
        path_minusculas = f"{output_files_path}\\minusculas"
        path_repeticiones = f"{output_files_path}\\ordenado_repeticiones"
        path_alfabeticos = f"{output_files_path}\\ordenado_alfabetico"
        path_dataframe_completo = f"{output_files_path}\\dataframe_completo"

        print("CONVERTIR MINUSCULAS START")
        self.convertirMinusculas(path_split_words, path_minusculas)
        print("CONVERTIR MINUSCULAS END")

        print("ARCHIVOS ORDENADOS ALFABETICAMENTE START")
        self.generar_archivos_frecuencia_alfabetica(path_minusculas, path_alfabeticos)
        print("ARCHIVOS ORDENADOS ALFABETICAMENTE END")

        print("ARCHIVOS ORDENADOS POR REPETICIONES START")
        self.generar_archivos_repeticiones(path_alfabeticos, path_repeticiones)
        print("ARCHIVOS ORDENADOS POR REPETICIONES END")

        print("AGREGAR INCIDENCIAS START")
        self.incidenciasOptMgr.agregar_incidencias(f"{path_repeticiones}\\repeticiones.txt", path_alfabeticos, path_dataframe_completo)
        print("AGREGAR INCIDENCIAS END")
        print("done")