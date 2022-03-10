import pandas as pd 
import os
import numpy as np

file_list = [
    '2010-2020-data/updated-orkney.csv',
    '2010-2020-data/updated-Dorset.json',
    '2010-2020-data/updated-cambridgeshire.csv',
    '2010-2020-data/updated-castle_point.csv',
    '2010-2020-data/updated-Ceredigion_store.json',
    '2010-2020-data/updated-cheshire_east.csv',
    '2010-2020-data/updated-Chiltern_store.json',
    '2010-2020-data/updated-chiltern_store.json',
    '2010-2020-data/updated-devon.csv',
    '2010-2020-data/updated-Dorset.json',
    '2010-2020-data/updated-flintshire.csv',
    '2010-2020-data/updated-forest_of_dean.csv',
    '2010-2020-data/updated-Fylde_outlet.csv',
    '2010-2020-data/updated-greater_london.csv',
    '2010-2020-data/updated-Greater_London.json',
    '2010-2020-data/updated-Haringgey.json',
    '2010-2020-data/updated-Kent_branch_.json',
    '2010-2020-data/updated-Lambeth_store.json',
    '2010-2020-data/updated-Larne_store.json',
    '2010-2020-data/updated-lincoln.csv',
    '2010-2020-data/updated-Newham_branch.json',
    '2010-2020-data/updated-North_Ayrshire.json'
    '2010-2020-data/updated-North_Yorkshire.json',
    '2010-2020-data/updated-peeblesshire.json',
    '2010-2020-data/updated-Sefton-outlet.json',
    '2010-2020-data/updated-staffordshire.csv',
    '2010-2020-data/updated-stoke_on_trent.csv',
    '2010-2020-data/updated-sussex.csv',
    '2010-2020-data/updated-swansea.csv',
    '2010-2020-data/updated-Tyne_and_Wear.json',
    '2010-2020-data/updated-warwick-branch.csv',
    '2010-2020-data/updated-wyre_branch.csv',
    '2013_Bassetlaw_outlet.csv']


data_folder= '2010-2020-data'
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
            file_df_pivot = file_df.pivot_table (index='product', columns=None, values='quantity',aggfunc = np.sum)
            file_df_pivot =  file_df_pivot.reset_index()
            print('created pivot:'+ file)
            file_df_pivot.to_csv('quantity/'+file.split('.')[0]+'.csv')
            print('saved:'+ file)
        except:
            print("error processing: "+file)


print('completed')



    