import dash
from github_info_header import github_info_header, html

app = dash.Dash(__name__)
app.layout = html.Div([
    github_info_header(),
    html.Img(src="assets/tvol_banner.png")
])

if __name__ == '__main__':
    app.run_server(debug=True)






