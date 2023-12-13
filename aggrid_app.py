'''
aggrid_app.py
'''
# aggrid_app.py
import dash
from dash import dcc, html
from callbacks import setup_callbacks
from data import create_data
from layouts import generate_ag_grid, generate_dropdown

class AgGridApp:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.setup_layout()
        self.setup_callbacks()
        self.data = create_data()
        self.dfs = {'all': self.data.all2, 'tenday': self.data.tenday2}

    def setup_layout(self):
        self.app.layout = html.Div([
            html.H1("WY Cattle"),
            generate_dropdown('dropdown-id', [{'label': key, 'value': key} for key in self.dfs.keys()]),
            generate_ag_grid('agg-all', self.data.all1.columns, initial_data=self.data.all2,
                             style={'height': '400px', 'display': 'block'}),
            generate_ag_grid('agg-tenday', self.data.tenday1.columns, initial_data=self.data.tenday2,
                             style={'height': '400px', 'display': 'none'}),
        ])

    def setup_callbacks(self):
        setup_callbacks(self.app)
