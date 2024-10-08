import process_data as pcd
import matplotlib.pyplot as plt
import numpy as np
import process as p

rel_t_step, files_sto = pcd.get_data_mode('sto')
rel_td_step, files_det = pcd.get_data_mode('det')


def csv_to_t(id, mode):
    f = f"data_{id}_{mode}"
    df = pcd.pd.read_csv(f"data\\data_files\\{f}.csv", header=None)
    df.columns = ['w','theta','qv','qr','qn','t','id','cd','qvs']
    df['t'] = df['t'] * 15
    return df


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


det_colors = {
    "w":"blue",
    "theta":"red",
    "qv":"lightgray",
    "qr":"lightblue",
    "qn":"orange",
    "cd":"magenta",
    "qz":"purple"
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
    fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=5, fancybox=True, shadow=True)
    return fig


def aero_detsto_plot(df,df_d):
    fig, ax = plt.subplots(ncols=2, nrows=2, sharey=True, figsize = (8,6))
    ax[0, 0].set_ylabel("Altura (km)")
    ax[1, 0].set_ylabel("Altura (km)")
    ax[0, 0].plot(df['w'],height, label = r"$w$", color = sto_colors['w'])
    ax[0, 0].plot(df_d['w'],height, color = det_colors['w'], linestyle = "dashed")
    ax[0, 0].set_ylim([0,15])
    ax[0, 0].set_xlim([-5,5])
    ax[0, 0].set_xlabel("Velocidad (m/s)")
    ax[0, 0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[0, 1].plot(df['theta'],height, label = r"$\theta'$", color = sto_colors['theta'])
    ax[0, 1].plot(df_d['theta'],height, color = det_colors['theta'], linestyle = "dashed")
    ax[0, 1].set_xlim([-5,5])
    ax[0, 1].set_xlabel(r"Pert.Temperatura ($\theta$)")
    ax[1, 0].plot(df['qv'], height, color = sto_colors['qv'], label = r"$q_v$")
    ax[1, 0].plot(df_d['qv'], height, color = det_colors['qv'], linestyle = "dashed")
    ax[1, 0].plot(df['qr'], height, color = sto_colors['qr'], label = r"$q_r$")
    ax[1, 0].plot(df_d['qr'], height, color = det_colors['qr'], linestyle = "dashed")
    ax[1, 0].set_xlabel(r"Agua (g/kg)")
    ax[1, 0].set_ylim([0,15])
    ax[1, 0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[1, 1].plot(df['qn'],height, label = r"$q_N$", color = sto_colors['qn'])
    ax[1, 1].plot(df_d['qn'],height, color = det_colors['qn'], linestyle = "dashed")
    ax[1, 1].set_xlabel(r"CCN ($p/cm^3$)")
    fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=5, fancybox=True, shadow=True)
    return fig


def Qzplot(df):
    fig, ax = plt.subplots(figsize = (8,6))
    qvs = [q_vs for q_vs in df['qvs']]
    ax.set_ylabel("Altura (km)")
    #ax.plot(df['qv'], height, color = "gray", label = r"$q_v$")
    #ax.plot(qvs, height, color = "purple", label = r"$q_{vs}$")
    qz = [qv - qvs[i] for i,qv in enumerate(df['qv'])]
    ax.plot(qz, height, color = sto_colors['qz'], label = r"$Q$")
    ax.plot([0,0], [0,15], 'k--', label = r"$0$")
    ax.set_xlabel("Proporción (g/kg)")
    ax.set_ylim([0,15])
    ax.set_yticks([0, 3, 6, 9, 12, 15])
    fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=5, fancybox=True, shadow=True)
    return fig


def cd_qn(df):
    qn = [x for x in df['qn']]
    cd = [s for s in df['cd']]
    fig, ax = plt.subplots(figsize = (8,6))
    ax.set_ylabel("Altura (km)")
    ax.plot(cd, height, color = sto_colors['cd'], label = r"$C_d$")
    ax.plot(qn, height, color = sto_colors['qn'], label = r"$q_N$")
    ax.set_ylim([0,15])
    ax.set_yticks([0, 3, 6, 9, 12, 15])
    fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=5, fancybox=True, shadow=True)
    return fig

result_plots = 0
if result_plots:
    times = [10,40,70]
    for t in times:
        r_t = rel_t_step[t] 
        r_t = round(r_t, 4)
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
            fig.savefig(f"fig_{p.data_origin}_{n}_{r_t}.png")


def inital_plot(mode):
    data_0 = csv_to_t(0, mode)
    height = np.linspace(0,15,len(data_0))
    fig1, ax = plt.subplots(ncols=2, nrows=1, figsize = (8,6),sharey = True)
    ax[0].plot(data_0['qn'] * 2, height, label = r"$q_N(0, z)$", color = sto_colors['qn'])
    ax[1].plot(data_0['qvs'], height, label = r"$q_{vs}(0, z)$", color = sto_colors['qvs'])
    ax[1].plot(data_0['qv'], height, label = r"$q_v(0, z)$", color = sto_colors['qv'])
    ax[0].set_xlabel('CCN (ppV)')
    ax[1].set_xlabel('q (g/kg)')
    ax[0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[0].set_ylim([0,15])
    ax[0].set_ylabel('Altura (km)')
    fig1.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=4, fancybox=True, shadow=True)
    return fig1

def plot_data_f(time_id, **kwargs):
    mode = kwargs.get('mode','sto')
    data_f = csv_to_t(time_id, mode)
    data_0 = csv_to_t(0, mode)
    height = np.linspace(0,15,len(data_0))
    fig2, ax = plt.subplots(nrows=2, ncols=3, figsize = (8, 6), sharey = True)
    ax[0, 0].set_ylabel("Altura (km)")
    ax[0, 0].plot(data_f['w'],height, label = r"$w$", color = sto_colors['w'])
    ax[0, 0].plot(data_0['w'],height, color = det_colors['w'], linestyle = "dashed")
    ax[0, 0].set_ylim([0,15])
    ax[0, 0].set_xlim([-5,5])
    ax[0, 0].set_xlabel("Velocidad Vert. (m/s)")
    ax[0, 0].set_yticks([0, 3, 6, 9, 12, 15])

    ax[0, 1].plot(data_f['theta'],height, label = r"$\theta'$", color = sto_colors['theta'])
    ax[0, 1].plot(data_0['theta'],height, color = det_colors['theta'], linestyle = "dashed")
    ax[0, 1].set_xlim([-5,5])
    ax[0, 1].set_xlabel(r"Pert.Temp.pot ($\theta$)")

    ax[0, 2].plot(data_f['cd'],height, label = r"$C_d'$", color = sto_colors['cd'])
    ax[0, 2].plot(data_0['cd'],height, color = det_colors['cd'], linestyle = "dashed")
    ax[1, 1].plot(data_f['qv'], height, color = sto_colors['qv'], label = r"$q_v$")
    ax[1, 1].plot(data_0['qv'], height, color = det_colors['qv'], linestyle = "dashed")
    ax[1, 1].set_xlabel(r"Vapor de Agua (g/kg)")
    ax[1, 1].set_ylim([0,15])

    ax[1, 2].plot(data_f['qr'], height, color = sto_colors['qr'], label = r"$q_r$")
    ax[1, 2].plot(data_0['qr'], height, color = det_colors['qr'], linestyle = "dashed")
    ax[1, 2].set_xlabel(r"Agua líquida (g/kg)")
    ax[1, 2].set_ylim([0,15])
    ax[1, 2].set_ylim([0, 5])


    ax[1, 0].set_ylabel("Altura (km)")
    ax[1, 0].set_yticks([0, 3, 6, 9, 12, 15])
    ax[1, 0].plot(data_f['qn'],height, label = r"$q_N$", color = sto_colors['qn'])
    ax[1, 0].plot(data_0['qn'],height, color = det_colors['qn'], linestyle = "dashed")
    ax[1, 0].set_xlabel(r"Aerosoles ($p/cm^3$)")
    fig2.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=6, fancybox=True, shadow=True)
    return fig2
"""
for i in range(80):
    fig = plot_data_f(i)
    fig.savefig(f"fig_gamma2\\fig_gamma2_{round(rel_t_step[i], 4)}.png")
    # plt.show()
"""

x = inital_plot('sto')
plt.show()