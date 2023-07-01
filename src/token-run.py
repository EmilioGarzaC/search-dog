import os
import time 
from modules.fase2Manager import fase2Manager

root = os.path.dirname(os.path.abspath(__file__))
output_files_path = os.path.join(root, "..", "output-files")
path_repeticiones = f"{output_files_path}\\ordenado_repeticiones"
path_alfabeticos = f"{output_files_path}\\ordenado_alfabetico"

fase2Mgr = fase2Manager()
startSplitSort = time.time()
fase2Mgr.generar_archivos_repeticiones(path_alfabeticos, path_repeticiones)
endSplitSort = time.time()
print(f"Tiempo tokenizacion :::::::::: {endSplitSort-startSplitSort}")