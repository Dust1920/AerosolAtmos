import os
import zipfile


if not os.path.exists("data\\data_files"):
    os.mkdir("data\\data_files")
folder_data = "data"
files = os.listdir(folder_data)

zip_files = []
for f in files:
    if f.endswith(".zip"):
        zip_files.append(f)

idx = 3

data_origin = zip_files[idx]
print(data_origin)
path_data = os.path.join(folder_data, data_origin)


with zipfile.ZipFile(path_data) as f:
    f.extractall("data\\data_files")