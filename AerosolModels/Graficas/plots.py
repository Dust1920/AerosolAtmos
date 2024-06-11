import process_data as pcd
import matplotlib.pyplot as plt
import numpy as np




rel_t_step, files_sto = pcd.get_data_mode('sto')
rel_td_step, files_det = pcd.get_data_mode('det')

def csv_to_t(id, mode):
    f = f"data_{id}_{mode}"
    df = pcd.pd.read_csv(f"data\\data_files\\{f}.csv", header=None)
    df.columns = ['w','theta','qv','qr','qn','t','id']
    df['t'] = df['t'] * 15
    return df

## Qvs








##


aerosol_model = csv_to_t(1,'sto')
aerosol_model_det = csv_to_t(1,'det')
print(aerosol_model)
height = np.linspace(0,15,len(aerosol_model))

def aero_plot(df):
    fig, ax = plt.subplots(ncols=2, nrows=2, sharey=True, figsize = (8,6))
    ax[0,0].plot(df['w'],height, label = r"$w$", color = "blue")
    ax[0,0].set_xlim([-5,5])
    ax[0,0].set_xlabel("Velocidad (m/s)")
    ax[0,1].plot(df['theta'],height, label = r"$\theta'$", color = "red")
    ax[0,1].set_xlim([-5,5])
    ax[0,1].set_xlabel(r"Pert.Temperatura ($\theta$)")
    ax[1,0].plot(df['qv'], height, color = "gray", label = r"$q_v$")
    ax[1,0].plot(df['qr'], height, color = "lightblue", label = r"$q_r$")
    ax[1,0].set_xlabel(r"Agua (g/kg)")
    ax[1,1].plot(df['qn'],height, label = r"$q_n$", color = "orange")
    ax[1,1].set_xlabel(r"CCN ($p/cm^3$)")
    fig.legend(loc='upper right', bbox_to_anchor=(1, 1))
    fig.tight_layout()
    return fig


def aero_detsto_plot(df,df_d):
    fig, ax = plt.subplots(ncols=2, nrows=2, sharey=True, figsize = (8,6))
    ax[0,0].plot(df['w'],height, label = r"$w$", color = "blue")
    ax[0,0].plot(df_d['w'],height, color = "gray", label = r"$w$ det")
    ax[0,0].set_xlim([-5,5])
    ax[0,0].set_xlabel("Velocidad (m/s)")
    ax[0,1].plot(df['theta'],height, label = r"$\theta'$", color = "red")
    ax[0,1].plot(df_d['theta'],height, color = "gray", label = r"$\theta'$ det")
    ax[0,1].set_xlim([-5,5])
    ax[0,1].set_xlabel(r"Pert.Temperatura ($\theta$)")
    ax[1,0].plot(df['qv'], height, color = "black", label = r"$q_v$")
    ax[1,0].plot(df_d['qv'], height, color = "gray", label = r"$q_v$ det")
    ax[1,0].plot(df['qr'], height, color = "lightblue", label = r"$q_r$")
    ax[1,0].plot(df_d['qr'], height, color = "gray", label = r"$q_r$ det")
    ax[1,0].set_xlabel(r"Agua (g/kg)")
    ax[1,1].plot(df['qn'],height, label = r"$q_r$", color = "orange")
    ax[1,1].plot(df_d['qn'],height, color = "gray", label = r"$q_r$ det")
    ax[1,1].set_xlabel(r"CCN ($p/cm^3$)")
    fig.legend(loc='upper right', bbox_to_anchor=(1, 1))
    fig.tight_layout()
    return fig

def Qzplot(df):
    fig, ax = plt.subplots()
    ax.plot(df['qv'], height, color = "gray", label = r"$q_v$")
    fig.legend()
    return fig


# fig_1 = aero_plot(aerosol_model)
# fig_2 = aero_detsto_plot(aerosol_model, aerosol_model_det)
fig = Qzplot(aerosol_model)
plt.show()