'''
app.py
'''
'''
aggrid_app.py
'''

import dash
from dash import dcc, html
import dash_ag_grid
from dash.dependencies import Input, Output

from callbacks import setup_callbacks

from data import CreateData
from styles import get_table_styles

dfs3 = {'all':'all',
            'tenday':'tenday',
            'status_col' : 'status_col'
            }

class AgGridApp:
    def __init__(self):
        self.app = dash.Dash(__name__)
 
        # self.all1, self.all2  = self.CreateData()
        # self.tenday1,self.tenday2= CreateData()
        # self.dfs1,self.dfs2 = CreateData()
        # self.status_col1, self.status_col2 = CreateData()
        self.data = CreateData()



        self.selected_table = None
        self.table_styles = get_table_styles()

        self.setup_layout()
        self.setup_callbacks()


    def generate_dropdown(self, dropdown_id, options):
        return dcc.Dropdown(
            id=dropdown_id,
            # value = default_val,
            options = options,
            style={'width': '50%'}
        )

    def generate_ag_grid(self, gen_grid_id, columns, initial_data=None):
        return dash_ag_grid.AgGrid(
            id=gen_grid_id,
            columnDefs=[{'headerName': col, 'field': col} for col in columns],
            rowData=initial_data if initial_data is not None else [],
            style=self.table_styles.get(gen_grid_id, {})
        )


    def setup_layout(self):
        

        dropdown_options = [{'label': key, 'value': key} for key in dfs3.keys()]

        self.app.layout = html.Div([
            html.H1("WY Cattle"),
            self.generate_dropdown('dropdown-id', dropdown_options),
        ] + [
            self.generate_ag_grid(table_id, df.columns, initial_data)
            for table_id, df, initial_data in [
                ('all', self.data.all1, self.data.all2),
                ('tenday', self.data.tenday1, self.data.tenday2),
                ('status_col', self.data.status_col1, self.data.status_col2),
                # Add more tables as needed
            ]
        ])

    def setup_callbacks(self):          #the update_table function is defined to take only the selected_table parameter,
                                        #and the decorator specifies that the value of the 'dropdown-id' component is the input triggering the callback.
        @self.app.callback(
            [   Output(table_id, 'style') for table_id in self.table_styles],
            [   Input('dropdown-id', 'value')]
        ) 

        def update_table(selected_table):
            table_styles = []
            for table_id in self.table_styles:
                if selected_table == table_id:
                    table_styles.append({'height': '400px', 'display': 'block'})
                else:
                    table_styles.append({'height': '400px', 'display': 'none'})
            return tuple(table_styles)


if __name__ == "__main__":
    aggApp = AgGridApp()
    aggApp.app.run_server(port=8081, debug=True)
