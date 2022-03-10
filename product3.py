import pandas as pd 
import os
import numpy as np

file_list = ['data 2011-2020/updated-.isle_of_white.csv', 'data 2011-2020/updated-belfast.csv','data 2011-2020/updated-braknell_forest.csv','data 2011-2020/updated-bracknell_forest.csv','data 2011-2020/updated-chorley.csv',
    'data 2011-2020/updated-east_lindsey.csv', 'data 2011-2020/updated-Falkirk_branch.json','data 2011-2020/updated-falkirk.csv','data 2011-2020/updated-fareham.csv','data 2011-2020/updated-Hampshire_branch.json', 'data 2011-2020/updated-harrow.csv',
    '2011-2020/updated-Hinckley_and_Bosworth_branch.json','data 2011-2020/updated-islington.csv','data 2011-2020/updated-norfolk.csv','data 2011-2020/updated-north_yorkshire.csv','2011-2020-data/updated-nottinghamshire.csv','data 2011-2020/updated-Oxford.json','data 2011-2020/updated-powyss.csv',
    'data 2011-2020/updated-rhoose.csv', 'data 2011-2020/updated-Richmondshire.json','data 2011-2020/updated-St_Edmundsburt.json','data 2011-2020-data/updated-west-somerset.csv']
    
data_folder= 'data 2011-2020'
file_list = os.listdir(data_folder)
    
for file in  file_list :
    print('reading data file')
    file_df = None
    if file.endswith('.csv'):
        file_df=pd.read_csv (data_folder+'/'+file)
            

    elif file.endswith('.json'):
        try: 
            file_df=pd.read_json(data_folder+'/'+file,lines=True)
        except:
            try:
                file_df=pd.read_json(data_folder+'/'+file)
            except:
                print('skipping '+file)
                    
    if file_df is not None :
        print('creating pivot:'+ file)
        try:
            file_df_pivot = file_df.pivot_table (index='product', columns=None, values='amount_in_gbp',aggfunc = np.sum)
            file_df_pivot =  file_df_pivot.reset_index()
            print('created pivot:'+ file)
            file_df_pivot.to_csv('pivot/'+file.split('.')[0]+'.csv')
            print('saved:'+ file)
        except:
            print("error processing: "+file)


print('completed')
