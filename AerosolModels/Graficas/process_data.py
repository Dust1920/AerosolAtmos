import os
import pandas as pd

folder_data = "data\\data_files"
files = os.listdir(folder_data)

mode = 'sto'


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