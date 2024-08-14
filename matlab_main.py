import matlab_to_pddf as m
import matplotlib.pyplot as plt


file = m.select(2)
print(file)

scales, df = m.mat_to_df(file)

print(df.columns)
height = df['z_axis'] * scales['Ls']
w_0 = df['w_ini'] * scales['Us']
w = df['w_np1'] * scales['Us']
thetap_0 = df['theta_prime_ini'] * scales['Ths']
thetap = df['theta_prime_np1'] * scales['Ths']
qv_0 = df['qv_ini'] * scales['qs']
qv = df['qv_ini'] * scales['qs']
qr_0 = df['qr_ini'] * scales['qs']
qr = df['qr_np1'] * scales['qs']
qn_0 = df['qN_ini'] * scales['qs']
qn = df['qN_np1'] * scales['qs']

plot_theta = [thetap, thetap_0]
plot_w = [w, w_0]
plot_qv = [qv, qv_0]
plot_qr = [qr, qr_0]
plot_qn = [qn, qn_0]

plots = [plot_w, plot_theta, plot_qv,
         plot_qn, plot_qr]
labels = [['w',None], [r'$\theta\'$',None], [r'$q_v$',None],
          [r'q_N',None], [r'q_r',None],['',None]]
colors = [["", 'black'],["", 'black'],["", 'black'],
          ["", 'black'],["", 'black'],["", 'black']]
linestyle = [[None,"dashed"],[None,"dashed"],[None,"dashed"],
             [None,"dashed"],[None,"dashed"],[None,"dashed"]]
def base_model(plots, **kwargs):
    max_cols = kwargs.get('max_col',3)
    figsize = kwargs.get('fig_size', (13, 8))
    v_color = kwargs.get('colors',None)
    v_label = kwargs.get('labels',None)
    v_ls = kwargs.get('linestyle',None)
    rows = len(plots) // max_cols + 1
    fig, ax = plt.subplots(ncols= max_cols, nrows= rows, figsize= figsize)
    for i in range(rows):
        for j in range(max_cols):
            lt = i*max_cols + j
            if lt == len(plots):
                break
            for pn, dist in enumerate(plots[lt]):
                ax[(i,j)].plot(dist, height,
                               color = v_color[lt][pn],
                               linestyle = v_ls[lt][pn],
                               label = v_label[lt][pn])

    return fig

base_model(plots)
plt.show()