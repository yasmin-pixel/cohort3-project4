import pandas as pd 
import numpy as np

all_df = pd.read_csv('branch_expenses_updated.csv')
all_df ['branch']= all_df['branch_name'].str.lower()
new = all_df['branch'].str.split(' ', n=3, expand=True)
all_df['branch']= np.where(all_df['branch_name'].str.strip().str.count(' ') >= 2, new[0]+'_'+new[1],new[0])

file_df_pivot = all_df.pivot_table (index='branch', columns=None, values='expense',aggfunc = np.sum)
file_df_pivot =  file_df_pivot.reset_index()
#print('created pivot')
file_df_pivot.to_csv('2010-2020-data/expenses1.csv')

data_for_branch =pd.read_csv('2010-2020-data/branch_name.csv')
cunnulative_data= data_for_branch.merge(file_df_pivot, how= 'inner',left_on= 'branch',right_on='branch') 
print(cunnulative_data)

cunnulative_data['profit']= cunnulative_data['amount_in_gbp']-cunnulative_data['expense']
cunnulative_data.to_csv('2010-2020-data/profit.csv')
print(all_df.tail(5))



