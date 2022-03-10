
import os 
import pandas as pd 
import numpy as np



def per_hour_pivot():
    dir_name='pivot'
    folder_content= os.listdir(dir_name)
    all_pivot_tables=[]
    for file in folder_content:
        print('reading'+ file)
        if file.endswith('.csv'):
                all_pivot_tables.append(pd.read_csv (dir_name + '/' + file))

    all_pivot_df = pd.concat(all_pivot_tables)
    try:
        file_df_pivot = all_pivot_df.pivot_table (index='hour', columns=None, values='amount_in_gbp',aggfunc = len)
        file_df_pivot =  file_df_pivot.reset_index()
        print('created pivot')
        file_df_pivot.to_csv('per_hour/per_hour_summary.csv')
        print('saved:')
    except :
        print('process failed')
    