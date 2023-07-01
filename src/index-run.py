import os
import time 
from modules.incidenciasOptMgr import incidenciasOptMgr

print("REPETICIONES: CUANTAS VECES APARECE EL TOKEN EN ESTE ARCHIVO")
print("INCIDENCIAS: EN CUANTOS ARCHIVOS SALE EL TOKEN")
root = os.path.dirname(os.path.abspath(__file__))
output_files_path = os.path.join(root, "..", "output-files")
path_repeticiones = f"{output_files_path}\\ordenado_repeticiones"
path_alfabeticos = f"{output_files_path}\\ordenado_alfabetico"
path_dataframe_completo = f"{output_files_path}\\dataframe_completo"

mgr = incidenciasOptMgr()
startSplitSort = time.time()
mgr.agregar_incidencias(f"{path_repeticiones}\\repeticiones.txt", path_alfabeticos, path_dataframe_completo)
endSplitSort = time.time()
print(f"Tiempo index :::::::::: {endSplitSort-startSplitSort}")