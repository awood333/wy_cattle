'''
layouts.py
'''
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_ag_grid


def generate_dropdown(dropdown_id, default_val):
    return dcc.Dropdown(
        id=dropdown_id,
        default_val = 'all',
        style={'width': '50%'}
    )

def generate_ag_grid(self, gen_grid_id, columns, initial_data=None, style=None):
    return dash_ag_grid.AgGrid(
        id=gen_grid_id,
        columnDefs=[{'headerName': col, 'field': col} for col in columns],
        rowData=initial_data if initial_data is not None else [],
        style=style if style is not None else {}
    )