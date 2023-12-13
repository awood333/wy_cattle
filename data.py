'''
data.py
'''
import pandas as pd

def create_data():

    date_cols = ['death_date', 'last stop date', 'last calf bdate', 'i_date', 'u_date', 'expected bdate']

    all1 = pd.read_csv('F:\\COWS\\data\\insem_data\\all.csv', parse_dates=date_cols)
    tenday1 = pd.read_csv('F:\\COWS\\data\\milk_data\\totals\\milk_aggregates\\tenday.csv')

    all2 = all1.to_dict('records')
    tenday2 = tenday1.to_dict('records')
    dfs = ['all1']

    return all1, all2, tenday1, tenday2