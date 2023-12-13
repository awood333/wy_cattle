import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_ag_grid
import pandas as pd

class AgGridApp:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        date_cols = ['death_date', 'last stop date', 'last calf bdate', 'i_date', 'u_date', 'expected bdate']

        all1 = pd.read_csv('F:\\COWS\\data\\insem_data\\all.csv', parse_dates=date_cols)
        tenday1 = pd.read_csv('F:\\COWS\\data\\milk_data\\totals\\milk_aggregates\\tenday.csv')

        all2 = all1.to_dict('records')
        tenday2 = tenday1.to_dict('records')
        # print(tenday2[0])

        self.dfs = {'all': all2, 'tenday': tenday2}

        self.app.layout = html.Div([
            html.H1("WY Cattle"),

            self.generate_dropdown('dropdown-id', [{'label': key, 'value': key} for key in self.dfs.keys()]),

            self.generate_ag_grid('agg-all', all1.columns, initial_data=all2,
                                  style={'height': '400px', 'display': 'block'}),
            self.generate_ag_grid('agg-tenday', tenday1.columns, initial_data=tenday2,
                                  style={'height': '400px', 'display': 'none'}),

            html.Div(id='debug-output')  # Add this line
        ])

    def generate_dropdown(self, dropdown_id, options):
        return dcc.Dropdown(
            id=dropdown_id,
            options=options,
            value=options[0]['value'],
            style={'width': '50%'}
        )

    def generate_ag_grid(self, gen_grid_id, columns, initial_data=None, style=None):
        # print(f"Columns for {gen_grid_id}: {columns}") 
        return dash_ag_grid.AgGrid(
            id=gen_grid_id,
            columnDefs=[{'headerName': col, 'field': col} for col in columns],
            rowData=initial_data if initial_data is not None else [],
            style=style if style is not None else {}
        )

    def setup_callbacks(self):
        @self.app.callback(
            [ Output('agg-all', 'style'),  \
             Output('agg-tenday', 'style')
            ], 

            [Input('dropdown-id', 'value')
             ]
        )
        def update_table(selected_table):
            print('Callback triggered with value:', selected_table)
            print('xxxxxxxxxxxxxxxxxx')

            if selected_table == 'all':
                print('all selected')
                return {'height': '400px', 'display': 'block'}, {'height': '400px', 'display': 'none'}
            elif selected_table == 'tenday':
                print('tenday selected')
                return {'height': '400px', 'display': 'none'}, {'height': '400px', 'display': 'block'}
            else:
              
                return {'height': '400px', 'display': 'none'}, {'height': '400px', 'display': 'none'}


if __name__ == "__main__":
    aggApp = AgGridApp()
    aggApp.app.run_server(port=8081, debug=True)  #, dev_tools_ui=True
    # server = agGridApp.setup_layout().server
    # server.run( host='0.0.0.0', port=8081, debug=True)




