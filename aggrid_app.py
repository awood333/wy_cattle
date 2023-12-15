# '''
# aggrid_app.py
# '''

# import dash
# from dash import dcc, html
# import dash_ag_grid

# from callbacks import setup_callbacks
# from data import create_data
# # from layouts import LayoutGenerator

# class AgGridApp:
#     def __init__(self):
#         self.app = dash.Dash(__name__)
#         self.all1, self.all2, self.tenday1, self.tenday2, self.dfs1, self.dfs2 = create_data()
#         # print("all2:", self.all2[0])
#         # print("tenday2:", self.tenday2[0])

        
#         self.setup_layout()
#         setup_callbacks(self.app)


#     def generate_dropdown(self, dropdown_id, options):

#         # options = [{'label': key, 'value': self.dfs2[key]} for key in self.dfs2.keys()]
#         # print("Dropdown options:", options)


#         return dcc.Dropdown(
#             id=dropdown_id,
#             # value = default_val,
#             options = options,
#             style={'width': '50%'}
#         )

#     def generate_ag_grid(self, gen_grid_id, columns, initial_data=None, style=None):
#         return dash_ag_grid.AgGrid(
#             id=gen_grid_id,
#             columnDefs=[{'headerName': col, 'field': col} for col in columns],
#             rowData=initial_data if initial_data is not None else [],
#             style=style if style is not None else {}
#         )

#     def setup_layout(self):
#         self.app.layout = html.Div([
#             html.H1("WY Cattle"),
#             self.generate_dropdown('dropdown-id', 
#                     [{'label': key, 'value': key} for key in self.dfs2.keys()]),

#             self.generate_ag_grid('all', self.all1.columns, initial_data=self.all2,
#                              style={'height': '400px', 'display': 'none'}),
            
#             self.generate_ag_grid('tenday', self.tenday1.columns, initial_data=self.tenday2,
#                              style={'height': '400px', 'display': 'none'}),
#         ])
