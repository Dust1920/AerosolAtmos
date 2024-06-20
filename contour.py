import matplotlib.pyplot as plt
import numpy as np
import process_data as pcd

def csv_to_t(id, mode):
    f = f"data_{id}_{mode}"
    df = pcd.pd.read_csv(f"data\\data_files\\{f}.csv", header=None)
    df.columns = ['w','theta','qv','qr','qn','t','id','cd']
    df['t'] = df['t'] * 15
    return df

mode = 'sto'
rel_t_step, files_sto = pcd.get_data_mode('sto')
variable = 'w'

d0 = csv_to_t(0, mode)
height = np.linspace(0,15, len(d0))
time = [rel_t_step[j] for j in range(80)]
contour = pcd.pd.DataFrame(index = height, columns = time)
for i in range(80):
    r_i = round(time[i],4)
    data = csv_to_t(i, mode)
    height = np.linspace(0,15, data.shape[0])
    print(contour)
    print(data)
    contour[r_i] = list(data[variable])

print(contour)

data = csv_to_t(5, mode)


