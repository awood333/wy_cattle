'''
layouts.py
'''
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import dash_ag_grid
# from data import create_data
# from aggrid_app import AgGridApp


# class LayoutGenerator:
#     def __init__(self, app):
#         self.app = app
#         self.all1, self.all2, self.tenday1, self.tenday2, self.dfs = create_data()
        


    
#     def generate_layout(self):
#         return html.Div([
#             html.H1("WY Cattle"),
#             self.generate_dropdown('dropdown-id', [{'label': key, 'value': key} for key in self.dfs.keys()]),
#             self.generate_ag_grid('agg-all', self.all1.columns, initial_data=self.all2,
#                                   style={'height': '400px', 'display': 'block'}),
#             self.generate_ag_grid('agg-tenday', self.tenday1.columns, initial_data=self.tenday2,
#                                   style={'height': '400px', 'display': 'none'}),
#         ])