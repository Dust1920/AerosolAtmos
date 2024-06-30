import scipy.io as scio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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



x = scio.loadmat("SlnT60.mat")

new_dict = {}
for k in x.keys():
    lenx = len(x[k])
    if lenx > 100:
        new_dict[k] = x[k]

df = pd.DataFrame()
for n_k, k in enumerate(new_dict.keys()):
    y = new_dict[k]
    print(y)
    data = [u[0] for u in y]
    if n_k == 0:
        df.index = np.array(data) * 10
        df.index.name = k
    else:
        df[k] = data

print(df)
print(df.columns)
matlab_fig, ax = plt.subplots(2,3, figsize = (8,6))
ax[0, 0].plot(df['w_np1'] * Us, df.index, label = r"$w$", color = sto_colors['w'])
ax[0, 0].plot(df['w_ini'] * Us, df.index, linestyle = "dashed", color = "black")
ax[0, 0].set_ylabel("Altura (km)")
ax[0, 0].set_xlabel("Velocidad Vert. (m/s)")
ax[0, 0].set_yticks([0, 5, 10, 15])
ax[0, 0].set_ylim([0, 15])
ax[0, 0].set_xlim([-10, 10])
ax[0, 1].plot(df['theta_prime_np1'] * Ths, df.index, label = r"$\theta'$", color = sto_colors['theta'])
ax[0, 1].plot(df['theta_prime_ini'] * Ths, df.index, linestyle = "dashed", color = "black")
# ax[0, 1].set_ylabel("Altura (km)")
ax[0, 1].set_xlabel("Pert.Temp.pot (K)")
ax[0, 1].set_yticks([0, 5, 10, 15])
ax[0, 1].set_ylim([0, 15])
ax[0, 1].set_xlim([-3, 8])
ax[0, 2].plot(df['theta_e'] * Ths, df.index, label = r"$\theta_e$", color = 'green')
ax[0, 2].plot(df['theta_e_ini'] * Ths, df.index, linestyle = "dashed", color = "black")
# ax[0, 2].set_ylabel("Altura (km)")
ax[0, 2].set_xlabel("Temp.Pot.equiv (K)")
ax[0, 2].set_yticks([0, 5, 10, 15])
ax[0, 2].set_ylim([0, 15])
ax[0, 2].set_xlim([300, 360])
ax[1, 0].plot(df['qN_np1'] * cnns, df.index, label = r"$q_N$", color = sto_colors['qn'])
ax[1, 0].plot(df['qN_ini'] * cnns, df.index, linestyle = "dashed", color = "black")
ax[1, 0].set_ylabel("Altura (km)")
ax[1, 0].set_xlabel("Aerosoles (ppV)")
ax[1, 0].set_yticks([0, 5, 10, 15])
ax[1, 0].set_ylim([0, 15])
ax[1, 0].set_xlim([0, 1000])
ax[1, 1].plot(df['qv_np1'] * qs, df.index, label = r"$q_v$", color = sto_colors['qv'])
ax[1, 1].plot(df['qv_ini'] * qs, df.index, linestyle = "dashed", color = "black")
# ax[1, 1].set_ylabel("Altura (km)")
ax[1, 1].set_xlabel("Vapor (g/kg)")
ax[1, 1].set_yticks([0, 5, 10, 15])
ax[1, 1].set_ylim([0, 15])
ax[1, 1].set_xlim([0, 30])
ax[1, 2].plot(df['qr_np1'] * qs, df.index, label = r"$q_r$", color = sto_colors['qr'])
ax[1, 2].plot(df['qr_ini'] * qs, df.index, linestyle = "dashed", color = "black")
ax[1, 2].set_xlabel("Lluvia (g/kg)")
# ax[1, 2].set_ylabel("Altura (km)")
ax[1, 2].set_yticks([0, 5, 10, 15])
ax[1, 2].set_ylim([0, 15])
ax[1, 2].set_xlim([0, 10])
matlab_fig.legend(loc = "upper center", ncols = 6, bbox_to_anchor = (0.5,0.95))
plt.savefig('matlab_plot.png')
plt.show()

df_copy = df.copy()
for c in df_copy.columns:
    if c.endswith('_ini'):
        df_copy.drop(columns=c, inplace=True)


print(df_copy)