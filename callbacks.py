'''
callbacks.py
'''

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def setup_callbacks(app):
    @app.callback(
        [ Output('agg-all', 'style'),
          Output('agg-tenday', 'style')
        ], 

        [ Input('dropdown-id', 'value')
            ]
    )
    def update_table(selected_table):
        print('Callback triggered with value:', selected_table)

        if selected_table == 'all':
            return {'height': '400px', 'display': 'block'}, {'height': '400px', 'display': 'none'}
        
        elif selected_table == 'tenday':
            return {'height': '400px', 'display': 'none'}, {'height': '400px', 'display': 'block'}
        
        else:
            
            return {'height': '400px', 'display': 'none'}, {'height': '400px', 'display': 'none'}
