import os
import pandas as pd

class incidenciasOptMgr:    
    #HISTORIA 11
    def agregar_incidencias(self, path_origen, path_comparativos, output_path):
        dataframe= pd.read_csv(path_origen)
        print(dataframe)
        # Agregar la nueva columna utilizando la función
        incidencias = self.generar_valores_incidencias(dataframe, path_comparativos)
        dataframe = self.agregar_columna(dataframe, 'INCIDENCIAS', incidencias)
        # Guardar el DataFrame actualizado  
        print(dataframe)
        with open(f'{output_path}\\dataframe_completo.txt', 'w') as new_file:
            new_file.write(dataframe.to_string())
        pass

    def agregar_columna(self, dataframe, nombre_columna, valores):
        dataframe[nombre_columna] = valores
        return dataframe

    # HISTORIA H12
    def generar_valores_incidencias(self, dataframe, path_comparativo):
        #genera una columna para un dataframe en la que aparece la cantidad de archivos que sale una palabra token
        incidencias = []
        #itera entre los primeros valores de cada renglon
        for token in dataframe["TOKEN"]:
            count = self.countAll(token, path_comparativo)
            incidencias.append(count)
        return incidencias

    def countAll(self, query, path):
        #abre cada archivo de un folder, busca si sale la palabra query, y si sale, le suma un 1 al valor de su cuenta.
        #luego, regresa esa cuenta
        fileList = os.listdir(path)
        count = 0
        for file_name in fileList:
            file_path = f"{path}\\{file_name}"
            count += self.countIn(query, file_path)
        return count
    
    def countIn(self, query, path):
        #lee todo un dataframe, revisa su primera columna, y si existe el query dentro de esa columna, regresa un uno
        df= pd.read_csv(path)
        if query in set(df.iloc[:, 0]):
            return 1
        else:
            return 0
        
