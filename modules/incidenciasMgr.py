import glob
import pandas as pd

class incidenciasMgr:
# HISTORIA H11
    def agregar_columna(dataframe, nombre_columna, valores):
        dataframe[nombre_columna] = valores
        return dataframe

    def agregar_incidencias(path, output_path):
        fileList = os.listdir(path)
        for file_name in fileList:
            path_folder = path
            path_archivo = f"{path}\\{file_name}"
            print("Contando incidencias en: " + path_archivo)
            agregarIncidencias_dataFrame(path_folder, path_archivo, output_path)

    def agregarIncidencias_dataFrame(path_folder, path_archivo, output_path):
        df= pd.read_csv(path_archivo)
        # Valores para la nueva columna
        valores_nueva_columna = generar_valores_incidencias(df, path_folder)
        # Agregar la nueva columna utilizando la función
        df_actualizado = agregar_columna(df, 'INCIDENCIAS', valores_nueva_columna)
        # Imprimir el DataFrame actualizado  
        file_name = (os.path.basename(path_archivo))
        file_name = file_name.replace("frecuencias", "incidencias")
        with open(f'{output_path}\\{file_name}', 'w') as new_file:
            new_file.write(df_actualizado.to_string())
        pass

    # HISTORIA H12
    def countIn(query, path):
        df= pd.read_csv(path)
        if query in set(df.iloc[:, 0]):
            return 1
        else:
            return 0

    def countAll(query, path):
        fileList = os.listdir(path)
        count = 0
        for file_name in fileList:
            file_path = f"{path}\\{file_name}"
            count += countIn(query, file_path)
        return count

    def generar_valores_incidencias(dataframe, path):
        incidencias = []
        for index, row in dataframe.iterrows():
            value = row[0]
            incidencias.append(countAll(value, path))
        return incidencias