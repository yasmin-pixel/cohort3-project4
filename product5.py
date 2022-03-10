import os 
import pandas as pd 
import numpy as np


dir_name='pivot'
folder_content= os.listdir(dir_name)
all_pivot_tables=[]
for file in folder_content:
    print('reading'+ file)
    if file.endswith('.csv'):
            all_pivot_tables.append(pd.read_csv (dir_name + '/' + file))

all_pivot_df = pd.concat(all_pivot_tables)
try:
    file_df_pivot = all_pivot_df.pivot_table (index='product', columns=None, values='amount_in_gbp',aggfunc = np.sum)
    file_df_pivot =  file_df_pivot.reset_index()
    print('created pivot')
    file_df_pivot.to_csv('pivot/summary.csv')
    print('saved:')
except e:
    print('process failed')
    print(e)

        
