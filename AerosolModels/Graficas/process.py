import os
import zipfile

folder_data = "data"
files = os.listdir(folder_data)
data_origin = files[0]
path_data = os.path.join(folder_data, data_origin)

if not os.path.exists("data\\data_files"):
    os.mkdir("data\\data_files")
with zipfile.ZipFile(path_data) as f:
    f.extractall("data\\data_files")