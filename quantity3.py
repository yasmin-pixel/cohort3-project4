import pandas as pd 
import os
import numpy as np

file_list = [
'2012-2020/updated-Wrexham_store.csv',
'2012-2020/updated-armagh.csv',
'2012-2020/updated-ballymoney.csv',
'2012-2020/updated-Bargoed.json',
'2012-2020/updated-Barry_outlet.json',
'2012-2020/updated-Bedford_Borough_branch.json',
'2012-2020/updated-Bedfordshire.json',
'2012-2020/updated-Bridgend_outlet.json',
'2012-2020/updated-Colcheseter.json',
'2012-2020/updated-darlington.csv',
'2012-2020/updated-Dumfries_and_Gallowa.json',
'2012-2020/updated-East_Dunbartonshire.json',
'2012-2020/updated-East_Hertfordshire.json',
'2012-2020/updated-edinburgh.csv',
'2012-2020/updated-glasgow.csv',
'2012-2020/updated-Hampshire_branch.json',
'2012-2020/updated-Hinckley_and_Bosworth_branch,json',
'2012-2020/updated-Isle_of_Anglesey.json',
'2012-2020/updated-Lancashire.json', 
'2012-2020/updated-Lincolnshire.json',
'2012-2020/updated-Neath_Port_Talbort.csv',
'2012-2020/updated-Reigate_and_Banstead.csv',
'2012-2020/updated-rushcliffe.csv',
'2012-2020/updated-Sevenoks.csv',
'2012-2020/updated-Shepway_store.csv',
'2012-2020/updated-West_Oxfordshire.csv',
'2012-2020/updated-Worcestershire.csv']
  
data_folder= '2012-2020'
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
