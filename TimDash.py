import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go


app = dash.Dash()

#app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

xs = pd.DataFrame(

app.layout = html.Div(children=[
    html.H1(children='DSL Dyno App'),
    dcc.Graph(
        id='DSL Scatter',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Force-Displacement'
            }
        }
    ),
    dcc.Slider(value=4, min=-10, max=20, step=0.5, marks={-5: '-5 Degrees', 0: '0', 10: '10 Degrees'}),
    html.Button('Click Me', id='my-button')
])


if __name__ == '__main__':
    app.run_server(debug=True)