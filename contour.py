import matplotlib.pyplot as plt
import numpy as np
import process_data as pcd
import process as p

def csv_to_t(id, mode):
    f = f"data_{id}_{mode}"
    df = pcd.pd.read_csv(f"data\\data_files\\{f}.csv", header=None)
    df.columns = ['w','theta','qv','qr','qn','t','id','cd','qvs']
    df['t'] = df['t'] * 15
    return df

mode = 'sto'
rel_t_step, files_sto = pcd.get_data_mode(mode)
variable = 'cd'

d0 = csv_to_t(0, mode)
height = np.linspace(0,15, len(d0))
time = [round(rel_t_step[j], 4) for j in range(80)]

"""
def atmos_contour(variable,**kwargs):
    unit = kwargs.get('unit', 'g/kg')
    name_variable = kwargs.get('name', variable)
    contour = pcd.pd.DataFrame(index = height, columns = time)
    for i in range(80):
        r_i = time[i]
        data = csv_to_t(i, mode)
        contour[r_i] = list(data[variable])
        try:
            x = time.index(r_i)
            print("x = ",x)
        except:
            print('NO',r_i)
    plt.contour(time, height,  contour)
    plt.xlabel('Tiempo (mins)')
    plt.ylabel('Altura (km)')
    plt.yticks([0, 3, 6, 9, 12, 15])
    plt.xticks([10 * i for i in range(7)])
    plt.title(f'{name_variable} {unit}')
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(f'contour_{variable}')
    plt.clf()



atmos_contour('qv', name = r"$q_v$")
atmos_contour('qr', name = r"$q_r$")
atmos_contour('qn', name = r"$q_N$")
atmos_contour('cd', unit = r'$g(kgs)^{-1}$', name = r"$C_d$")
"""


def atmos_contour(variable,ax = None, **kwargs):
    unit = kwargs.get('unit', 'g/kg')
    name_variable = kwargs.get('name', variable)
    contour = pcd.pd.DataFrame(index = height, columns = time)
    for i in range(80):
        r_i = time[i]
        data = csv_to_t(i, mode)
        contour[r_i] = list(data[variable])
        try:
            x = time.index(r_i)
            print("x = ",x)
        except:
            print('NO',r_i)
    countour_plot = ax.contour(time, height,  contour, 100)
    ax.set_xlabel('Tiempo (mins)')
    ax.set_ylabel('Altura (km)')
    ax.set_yticks([0, 3, 6, 9, 12, 15])
    ax.set_xticks([10 * i for i in range(7)])
    ax.set_title(f'{name_variable} {unit}')
    plt.colorbar(countour_plot, ax = ax)


print(p.data_origin)

fig, axs = plt.subplots(2, 2, figsize=(8, 6))  # Crear una figura con 2 subgráficos
# Llamar a la función atmos_contour para cada subgráfico
atmos_contour('w', ax=axs[0,0], name = r"$w$", unit = r"m$s^{-1}$")
atmos_contour('qr', ax=axs[0,1], name = r"$q_r$")
atmos_contour('qn', ax=axs[1,0], name = r"$q_N$")
atmos_contour('theta', ax=axs[1,1], name = r"$\theta'$", unit = r"$K$")
plt.tight_layout()
plt.show()