'''
    check_hive_results
    This function reads stdout file which contains target data.Target data is loaded in dataframe.
'''

import subprocess, sys
from config import *
from azure.storage.blob import *
import pandas as pd
import datetime
import os

def check_hive_results(self,dir):
        LOCALFILENAME = "/".join(os.getcwd().strip("/").split('/')[:3]) + '\Scripts\stdout'        
        results = None
        try:
            #print("Records from Target")   
                  
            results=pd.read_csv(LOCALFILENAME, sep="\t",parse_dates=True,infer_datetime_format= True,keep_default_na=False,dtype=str)
            results.rename(columns = lambda x: x.upper(),inplace=True)
            #results.rename(columns = lambda x: x.split(".")[1].upper(),inplace=True)
            results = results.applymap(lambda x: str(x).split(".")[0] if isinstance(x, object) else x)                       
            #print("Hive Data loaded")
        except Exception as error:
            print("Exception occured in Readtable.from_sqlserver_mstdb")            
            print('Caught this error: ' + str(error))
        return results





