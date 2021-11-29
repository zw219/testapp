import dash
from dash import html

# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
cwd = "Current working directory: {0}".format(cwd)

app = dash.Dash(__name__)
app.layout = html.Div([html.P(cwd), html.Img(src="assets/richZhangs_banner.png")])

if __name__ == '__main__':
    app.run_server(debug=True)
