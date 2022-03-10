import pandas as pd 
import numpy as np

def file_title (file_name):
    return file_name.split('updated-')[1].replace('.csv','').replace('.json','')





file_sales=['2010-2020-data/updated-bassetlaw.csv',
'2010-2020-data/updated-east_cambridgeshire.csv',
'2010-2020-data/updated-castle_point.csv',
'2010-2020-data/updated-orkney.csv',
'2010-2020-data/updated-cheshire_east.csv',
'2010-2020-data/updated-Fylde.csv',
'2010-2020-data/updated-lincoln.csv',
'2010-2020-data/updated-devon.csv',
'2010-2020-data/updated-flintshire.csv',
]
all_df= []
for file  in file_sales:
    df= pd.read_csv(file)
    branch_name = file_title(file)
    df['branch']= branch_name
    all_df.append(df)
    
all_df = pd.concat(all_df)
try:
    file_df_pivot = all_df.pivot_table (index='branch', columns=None, values='amount_in_gbp',aggfunc = np.sum)
    file_df_pivot =  file_df_pivot.reset_index()
    print('created pivot')
    file_df_pivot.to_csv('2010-2020-data/branch_name.csv')
    print('saved:')
except Exception as e:
    print('process failed')
    print(e)



