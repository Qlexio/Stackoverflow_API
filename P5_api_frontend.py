from dash import Dash, dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input, Output
import requests

app = Dash(__name__)

app.layout = html.Div(style={"backgroundColor": "#111111"}, 
    children=[
    html.H2("API de prédiction de Tags", style= {"textAlign": "center", 
        "color": '#7FDBFF'}),
    html.Div([
        html.Div(children= ["Titre: "], style= {"color": "#ffffff"}),
        html.Div(children= [dcc.Input(id='title', value='Titre', type='text')])
    ]),
    html.Br(),
    html.Div([
        html.Div(children= ["Post: "], style= {"color": "#ffffff"}),
        # html.Div(children= [html.Textarea(id='post', placeholder='Post')])
        html.Div(children= [dcc.Input(id='post', value='Post', type='text', 
            style= {"width": "400px", "height": "250px"})])
    ]),
    html.Br(),
    html.Div(id='my-output', style= {"color": '#7FDBFF'}),

    ]
)


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='title', component_property='value'),
    Input(component_id='post', component_property='value')
)
def update_output_div(title, post):
    texte = title.lower() + " " + post.lower()
    url = "http://127.0.0.1:8000/" + texte
    requete = requests.get(url)
    if requete.status_code == 200:
        return 'Output: {}'.format(requete.text)
    else:
        return "There is an error... :("


if __name__ == '__main__':
    app.run_server(debug=True)