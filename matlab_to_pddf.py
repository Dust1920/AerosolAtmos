import os
import scipy.io as scio
import pandas as pd

def console_space():
    print("#" * 80)

"""
Leer archivos Matlab y convertirlos en un dataframe de pandas. 
"""

matlab_files_folder = "matlab_files"
matlab_files = os.listdir(matlab_files_folder)
matlab_files = [x for x in matlab_files if x.endswith('.mat')]
print("Archivos disponibles\n", matlab_files)
console_space()
select_file = 2
file = matlab_files[select_file]
print("Archivo Seleccionado: ", file)
console_space()
path_file = os.path.join(matlab_files_folder, file)
raw = scio.loadmat(path_file)
print(raw.keys())
console_space()

# Eliminamos las variables ajenas al modelo. 
valid_keys = [k for k in raw.keys() if not k.endswith("_")]
print("Variables disponibles\n", valid_keys)
console_space()

one_l = {}  # Para las claves de tamaño 1 (Valores)
more_l = {} # Para las claves de tamaño mayor a 1 (Listas, Vectores, entre otros)
for vk in valid_keys:
    if len(raw[vk]) == 1:
        one_l[vk] = raw[vk][0][0]
    else:
        more_l[vk] = [r[0] for r in raw[vk]] # Si son listas, vectores, tuplas.


df = pd.DataFrame(more_l)  # Convertimos en un df
print("Valores uni-D\n", one_l)  # D de Dimensional
print("Valores multi-D", df)



"""
Funciones finales:
    * Seleccion de Archivo
    * Conversión Matlab File (.mat) to Pandas DataFrame (df)

"""

def select(code, **kwargs):
    folder = kwargs.get('folder',"matlab_files")
    extension = kwargs.get('ext','.mat')
    ext_files = [x for x in matlab_files if x.endswith(extension)]
    file = ext_files[code]
    print("Archivo Seleccionado: ", file)
    path = os.path.join(folder, file)
    return path

def mat_to_df(matlab_file):
    raw = scio.loadmat(matlab_file)

    valid_keys = [k for k in raw.keys() if not k.endswith("_")]

    one_l = {}  # Para las claves de tamaño 1 (Valores)
    more_l = {} # Para las claves de tamaño mayor a 1 (Listas, Vectores, entre otros)
    for vk in valid_keys:
        if len(raw[vk]) == 1:
            one_l[vk] = raw[vk][0][0]
        else:
            more_l[vk] = [r[0] for r in raw[vk]] # Si son listas, vectores, tuplas.

    df = pd.DataFrame(more_l)  # Convertimos en un df
    return one_l, df
