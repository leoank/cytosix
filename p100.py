# Read GCT file to extract names of all pertubation 
import pandas as pd 

def read_gct(file_path):
    with open(file_path, 'r') as file:
        version = file.readline().strip()
        dims = file.readline().strip()  #num of rows and cols

    # Convert the dim into row and col counts 
    num_rows, num_cols, *rest = map(int, dims.split())

    df = pd.read_csv(file_path, sep='\t', skiprows=2)
    return version, num_rows, num_cols, df


gct_file = '20240917_gct_v1.3.gct'
version, num_rows, num_cols, gct_df = read_gct(gct_file)

print(gct_df.pert_iname)
#gct_df.pert_iname.to_csv('gct_v1.3_pert_iname.csv')
sub_df = gct_df[['pert_iname','MOA', 'pert_id', 'id']] 
sub_df.to_csv('gct_v1.3_pert_iname.csv')