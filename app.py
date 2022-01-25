from dash import *
from testapp import *

app = Dash(__name__)
app.layout = html.Div([
    github_info_header(),
    html.Img(src="assets/burb.jpeg")
])

if __name__ == '__main__':
    app.run_server(debug=True)






