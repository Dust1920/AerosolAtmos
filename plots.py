import process_data as pcd
import matplotlib.pyplot as plt
import numpy as np


rel_t_step, files_sto = pcd.get_data_mode('sto')
rel_td_step, files_det = pcd.get_data_mode('det')


def csv_to_t(id, mode):
    f = f"data_{id}_{mode}"
    df = pcd.pd.read_csv(f"data\\data_files\\{f}.csv", header=None)
    df.columns = ['w','theta','qv','qr','qn','t','id','cd']
    df['t'] = df['t'] * 15
    return df

## Qvs
qvs_0 = 20
qvs_0 = qvs_0 / 1000


gamma = 1
tau_cr= 1


def q_vs(z):
    a0 = 18.04 # km
    a1 = 3.27  # km
    a2 = 0.1   # km
    a4 = 1-3.48
    pz = (1- a1 * np.log(1 + a2 * z)) ** a4
    q = (qvs_0 / pz)*np.exp(- a0 * ( 1 / ((1 - a1 * np.log(1 + a2*z)) * (1 + a2 * z)) - 1 ))
    # g/kg / km ** 3.48
    return q


def tau_c_inv(qn):
    nm = (qn/1000 - 0.5) / gamma
    tc = np.exp(-nm ** 2) * tau_cr
    tc = 1
    return tc


def condensation(qv, qvs, qn):
    # cd = np.max([qv - qvs,0])*tau_c_inv(qn)
    cd = (qv - qvs)*tau_c_inv(qn)
    return cd


sto_colors = {
    "w":"blue",
    "theta":"red",
    "qv":"lightgray",
    "qr":"lightblue",
    "qn":"orange",
    "cd":"magenta",
    "qz":"purple"
}


det_colors = {
    "w":"black",
    "theta":"black",
    "qv":"black",
    "qr":"black",
    "qn":"black",
    "cd":"black",
    "qz":"black"
}


def aero_plot(df):
    fig, ax = plt.subplots(ncols=2, nrows=2, sharey=True, figsize = (8,6))
    ax[1, 0].set_ylabel("Altura (km)")
    ax[0, 0].set_ylabel("Altura (km)")
    ax[0, 0].plot(df['w'],height, label = r"$w$", color = sto_colors['w'])
    ax[0, 0].set_xlim([-5, 5])
    ax[0, 0].set_xlabel("Velocidad (m/s)")
    ax[0, 0].set_ylim([0, 15])
    ax[0, 0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[0, 1].plot(df['theta'],height, label = r"$\theta'$", color = sto_colors['theta'])
    ax[0, 1].set_xlim([-5, 5])
    ax[0, 1].set_xlabel(r"Pert.Temperatura ($\theta$)")
    ax[1, 0].plot(df['qv'], height, color = sto_colors['qv'], label = r"$q_v$")
    ax[1, 0].plot(df['qr'], height, color = sto_colors['qr'], label = r"$q_r$")
    ax[1, 0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[1, 0].set_xlabel(r"Agua (g/kg)")
    ax[1, 0].set_ylim([0, 15])
    ax[1, 1].plot(df['qn'],height, label = r"$q_n$", color = sto_colors['qn'])
    ax[1, 1].set_xlabel(r"CCN ($p/cm^3$)")
    fig.legend(loc='upper right', bbox_to_anchor=(1, 1))
    fig.tight_layout()
    return fig


def aero_detsto_plot(df,df_d):
    fig, ax = plt.subplots(ncols=2, nrows=2, sharey=True, figsize = (8,6))
    ax[0, 0].set_ylabel("Altura (km)")
    ax[1, 0].set_ylabel("Altura (km)")
    ax[0, 0].plot(df['w'],height, label = r"$w$", color = sto_colors['w'])
    ax[0, 0].plot(df_d['w'],height, color = det_colors['w'], label = r"$w$ det")
    ax[0, 0].set_ylim([0,15])
    ax[0, 0].set_xlim([-5,5])
    ax[0, 0].set_xlabel("Velocidad (m/s)")
    ax[0, 0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[0, 1].plot(df['theta'],height, label = r"$\theta'$", color = sto_colors['theta'])
    ax[0, 1].plot(df_d['theta'],height, color = det_colors['theta'], label = r"$\theta'$ det")
    ax[0, 1].set_xlim([-5,5])
    ax[0, 1].set_xlabel(r"Pert.Temperatura ($\theta$)")
    ax[1, 0].plot(df['qv'], height, color = sto_colors['qv'], label = r"$q_v$")
    ax[1, 0].plot(df_d['qv'], height, color = det_colors['qv'], label = r"$q_v$ det")
    ax[1, 0].plot(df['qr'], height, color = sto_colors['qr'], label = r"$q_r$")
    ax[1, 0].plot(df_d['qr'], height, color = det_colors['qr'], linestyle = "dashed", label = r"$q_r$ det")
    ax[1, 0].set_xlabel(r"Agua (g/kg)")
    ax[1, 0].set_ylim([0,15])
    ax[1, 0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[1, 1].plot(df['qn'],height, label = r"$q_N$", color = sto_colors['qn'])
    ax[1, 1].plot(df_d['qn'],height, color = det_colors['qn'], label = r"$q_N$ det")
    ax[1, 1].set_xlabel(r"CCN ($p/cm^3$)")
    fig.legend(loc='upper right', bbox_to_anchor=(1, 1))
    fig.tight_layout()
    return fig


def Qzplot(df):
    fig, ax = plt.subplots(figsize = (8,6))
    qvs = [q_vs(z / 10) * 1000 for z in height]
    ax.set_ylabel("Altura (km)")
    #ax.plot(df['qv'], height, color = "gray", label = r"$q_v$")
    #ax.plot(qvs, height, color = "purple", label = r"$q_{vs}$")
    qz = [qv - qvs[i] for i,qv in enumerate(df['qv'])]
    ax.plot(qz, height, color = sto_colors['qz'], label = r"$Q$")
    ax.plot([0,0], [0,15], 'k--', label = r"$0$")
    ax.set_xlabel("Proporción (g/kg)")
    ax.set_ylim([0,15])
    ax.set_yticks([0, 3, 6, 9, 12, 15])
    fig.legend()
    return fig


def cd_qn(df):
    qvs = [q_vs(z / 10) for z in height]
    qv = [x for x in df['qv']]
    qn = [x for x in df['qn']]
    cd = [condensation(qv[i], qvs, qn[i]) * 10 for i,qvs in enumerate(qvs)]
    fig, ax = plt.subplots(figsize = (8,6))
    ax.set_ylabel("Altura (km)")
    ax.plot(cd, height, color = sto_colors['cd'], label = r"$10C_d$")
    ax.plot(qn, height, color = sto_colors['qn'], label = r"$q_N$")
    ax.set_ylim([0,15])
    ax.set_yticks([0, 3, 6, 9, 12, 15])
    fig.legend()
    fig.tight_layout()
    return fig


times = [10,40,70]
for t in times:
    r_t = rel_t_step[t] 

    t = t % 80
    aerosol_model = csv_to_t(t,'sto')
    aerosol_model_det = csv_to_t(t,'det')
    height = np.linspace(0,15,len(aerosol_model))

    fig_1 = aero_plot(aerosol_model)
    fig_2 = aero_detsto_plot(aerosol_model, aerosol_model_det)
    fig_3 = Qzplot(aerosol_model)
    fig_4 = cd_qn(aerosol_model)

    figs_t = [fig_1, fig_2,fig_3,fig_4]
    for n, fig in enumerate(figs_t):
        fig.savefig(f"fig_{n}_{r_t}.png")


