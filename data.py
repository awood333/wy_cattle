'''
data.py
'''
import pandas as pd
class CreateData():
        def __init__(self):
        
                self.all1, self.all2                    = self.create_all()
                self.tenday1,self.tenday2               = self.create_tenday()
                self.status_col1, self.status_col2      = self.create_status_col()

                self.dfs1,self.dfs2                     = self.create_dfs()

        def create_all(self):
                date_cols = ['death_date', 'last stop date', 'last calf bdate', 'i_date', 'u_date', 'expected bdate']

                all1a = pd.read_csv('F:\\COWS\\data\\insem_data\\all.csv', parse_dates=date_cols)
                all1=all1a.iloc[:, :].copy()
                all2        = all1            .to_dict(orient='records')
                return all1, all2
                
        def create_tenday(self):
                tenday1 = pd.read_csv('F:\\COWS\\data\\milk_data\\totals\\milk_aggregates\\tenday.csv')
                tenday2     = tenday1         .to_dict(orient='records')
                return tenday1, tenday2


        def create_status_col(self):
                status_col1 = pd.read_csv('F:\\COWS\\data\\status\\status_col.csv')
                status_col2 = status_col1     .to_dict(orient='records')
                return status_col1, status_col2

        def create_dfs(self):
                dfs1 = {'all': pd.DataFrame(self.all2), 
                        'tenday': pd.DataFrame(self.tenday2),
                        'status_col' : pd.DataFrame(self.status_col2)
                        }
                dfs2 = {'all':'all',
                        'tenday':'tenday',
                        'status_col' : 'status_col'
                        }
                
                return dfs1, dfs2