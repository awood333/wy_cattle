from aggrid_app import AgGridApp

if __name__ == "__main__":
    aggApp = AgGridApp()
    aggApp.app.run_server(port=8081, debug=True)
