'''
callbacks.py
'''

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def setup_callbacks(app):
    @app.callback(
        [ Output('all', 'style'),
          Output('tenday', 'style')
        ], 

        [ Input('dropdown-id', 'value')
            ]
    )
    def update_table(selected_table):
        print('Callback triggered with value:', selected_table)

        if selected_table == 'all':

            print('all selected')

            return {'height': '400px', 'display': 'none'}, {'height': '400px', 'display': 'none'}
        
     
        
        
        elif selected_table == 'tenday':
            return {'height': '400px', 'display': 'none'}, {'height': '400px', 'display': 'block'}
        

            print('tenday selectd')
        
        else:
            
            return {'height': '400px', 'display': 'none'}, {'height': '400px', 'display': 'none'}
