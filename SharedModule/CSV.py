import os
import pandas as pd

class CSV:
    def __init__(self,location):
        self.provided_location = location
        self.locations = {'DB1':f'{self.provided_location}/Previous_Snapshot.csv',
                          'DB2':f'{self.provided_location}/New_Snapshot.csv'}
        
    def GET(self,file_name):
        for i,j in self.locations.items():
            if i in file_name:
                return pd.read_csv(self.locations[i])
        return pd.DataFrame()
    
    def SET(self,file_name,data:pd.DataFrame):
        path_name = f'{self.provided_location}/{file_name}.csv'
        data.to_csv(path_name,index=False)
        self.locations[file_name] = path_name









