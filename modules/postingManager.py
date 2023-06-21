import os
import pandas as pd

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
                        #repeticiones = alpha_df.loc[alpha_df['REPETICIONES'] == token, 'REPETICIONES']
                        repeticiones = alpha_df[alpha_df.TOKEN==token].REPETICIONES.item()
                        new_col = pd.DataFrame({"DOCUMENTO":[file.replace("_modificado_frecuencias.txt", ".html")],
                                                "REPETICIONES":[repeticiones]})
                        posting_df = posting_df._append(new_col, ignore_index = True)
        print(posting_df)
        with open(f'{output_path}\\posting.txt', 'w') as new_file:
            new_file.write(posting_df.to_string())
        pass
    print("e")
            