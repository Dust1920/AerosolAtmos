import scipy.io as scio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

Ths = 3
qs = 1000
Us = 11.11
Ls = 10
Ts = 15
cnns = 1000

sto_colors = {
    "w":"blue",
    "theta":"red",
    "qv":"lightgray",
    "qr":"lightblue",
    "qn":"orange",
    "cd":"magenta",
    "qvs": "purple",
    "qz":"purple"
}

files = os.listdir("matlab_files")
path_files = [os.path.join("matlab_files", file) for file in files]

def matlab_to_pandas(matlab_file):
    new_dict = {}
    for k in matlab_file.keys():
        lenx = len(matlab_file[k])
        if lenx > 100:
            new_dict[k] = matlab_file[k]

    df = pd.DataFrame()
    for n_k, k in enumerate(new_dict.keys()):
        y = new_dict[k]
        data = [u[0] for u in y]
        if n_k == 0:
            df.index = np.array(data) * 10
            df.index.name = k
        else:
            df[k] = data
    return df

matfile = scio.loadmat(path_files[0])
df_1 = matlab_to_pandas(matfile)

print(df_1)

"""
for lf, f in enumerate(files):
    fig_name = f + ".png"
    path = path_files[lf]
    matf = scio.loadmat(path)
    df = matlab_to_pandas(matf)
    matlab_3dplot(df, fname = fig_name)
"""