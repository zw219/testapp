import dash
from dash import html
import git
from datetime import datetime
import os

repo = git.Repo(search_parent_directories=True)
repo_branch = repo.head.ref.path
repo_hash   = repo.head.object.hexsha
repo_msg    = repo.head.commit.message
repo_author = repo.head.commit.author.name
repo_dt     = datetime.fromtimestamp(repo.head.commit.committed_date).strftime(
    "%A, %d %b %Y at %H:%M:%S"
)

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
cwd = "Current working directory: {0}".format(cwd)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.P(cwd),
    html.P(repo_branch),
    html.P(repo_hash),
    html.P(repo_msg),
    html.P(repo_author),
    html.P(repo_dt),
    html.Img(src="assets/tvol_banner.png")
])

if __name__ == '__main__':
    app.run_server(debug=True)






