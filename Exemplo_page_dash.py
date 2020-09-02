import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import pandas as pd 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets = external_stylesheets)

def gera_planilha(dataframe): 
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(len(dataframe))
        ])
    ])

#Mudar a cor do fundo além de mudar a cor do texto na aplicação Web
colors = {
    'background':'#8FBC8F',
    'text':'#11111'
}

data = {f'col{val}': list(np.arange(1,21)*val) for val in range(1,21)}
# print(data)
df = pd.DataFrame(data=data)
# print(df.head())

app.layout = html.Div(children=[

    html.H1(
        ['Layout com Gráfico'], style={'textAlign':'center', 'color':colors['text']}
    ),

    html.Div(children='''
        Universidade Federal da Paraíba.
        Engenharia Elétrica.
    ''',
        style={'textAlign':'center', 'color': colors['text'] }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x':[1,2,3], 'y': [4,1,2],'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),

    html.H1('Tabela teste gerada com o componente html.Table'),

    gera_planilha(df),

    ],
    style= {'background':colors['background']}
)

if __name__ == '__main__':
    app.run_server(debug=True)