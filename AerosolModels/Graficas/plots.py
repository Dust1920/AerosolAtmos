import process_data as pcd

rel_t_step = pcd.dict_t_id
files = pcd.files_mode
print(rel_t_step)

def csv_to_t(id):
    f = f"data_{id}_{pcd.mode}"
    df = pcd.pd.read_csv(f"data\\data_files\\{f}.csv", header=None)
    df.columns = ['w','theta','qv','qr','qn','t','id']
    return df




x = csv_to_t(0)
print(x)