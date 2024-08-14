import os
import pandas as pd
import zipfile

# Folder de Origen de Archivos 
folder_data = "data\\data_files"
## Si no existe, creala. 
if not os.path.exists(folder_data):
    os.mkdir(folder_data)

folder_rawdata = "data"
files = os.listdir(folder_rawdata)

zip_files = []
for f in files:
    if f.endswith(".zip"):
        zip_files.append(f)

idx = -1

data_origin = zip_files[idx]

path_data = os.path.join(folder_data, data_origin)
with zipfile.ZipFile(path_data) as f:
    f.extractall(folder_data)

print(data_origin)

files = os.listdir(folder_data)

def get_data_mode(mode):
    files_mode = []

    for f in files:
        try:
            if f.index(mode):
                files_mode.append(f)
        except:
            continue

    dict_t_id = {}
    fm = len(files_mode)
    for i in range(fm):
        try:
            if files_mode.index(f"data_{i}_{mode}.csv") >= 0 :
                idf = files_mode.index(f"data_{i}_{mode}.csv")
                df = pd.read_csv(f"data\\data_files\\{files_mode[idf]}", header=None)
                dict_t_id[i] = df[5].unique()[0] * 15
        except:
            continue
    return dict_t_id, files_mode