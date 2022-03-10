import os 
import pandas as pd 
import numpy as np





def per_hour_sales() :

    per_hour_2010 = per_hour_2010.pivot_table(index='hour', columns=None, values= 'amount', aggfunc= len)
    per_hour_2010_df_pivot =   per_hour_2010_df_pivot .reset_index()
    return px.scatter( per_hour_2010_df_pivot.head(10),x='hour', y='amount')

 



            









    
