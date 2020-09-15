import plotly.graph_objects as go

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from apps import app_dashboard_v01

def init_user_data():
    return {
        'tipo':'Gráfico de Linha',
        'col-y': None,
        'col-x': None,
    }

def gera_layout():

    tipos_graf = [
        'Gráfico de Linha',
        'Gráfico de Barra Agrupado',
        'Gráfico de Barra Empilhado',
        'Histograma',
        'Box Plot',
    ]
            
    return html.Div([
        
        html.H2(
            ['Gráfico das Series'], className='title_style',
        ),

        html.Hr(className='hr'),

        html.Div([

                html.Div([

                        html.H6(
                            ['Visualização:'], className='subtitle_style',
                        ),

                        dcc.Dropdown(
                            id='type-graf',
                            options=[
                                {
                                    'label': tipo,
                                    'value': tipo,
                                }
                                for tipo in tipos_graf
                            ],
                            value = app.dict_apps['app_dashboard_v01']['user_data_graph']['tipo']
                        )
                    ],
                    style={'margin-left': '5px','width':'65%'}
                ),

                html.Div(id='options-dropdown-column')
            ],
            style={
                'width':'25%',
                'display':'inline-block',
                'float':'left'
            }
        ),
        
        html.Div(
            id='graph-position',
            style={
                'display':'inline-block',
                'float':'right',
                'width':'75%'
            }
        )
    ])

def gera_dropdowns_columns(tipograf,df):

    series = df.columns
    #[x,y]
    disabled_dropdown = [True,True]
    
    if tipograf in ['Histograma','Box Plot']:  
        defaultx = None
        disabled_dropdown[1] = False
        
    elif tipograf is None:
        defaultx = None

    else:
        defaultx = series[0] if app.dict_apps['app_dashboard_v01']['user_data_graph']['col-x'] is None \
            else app.dict_apps['app_dashboard_v01']['user_data_graph']['col-x']
        disabled_dropdown[0] = False
        disabled_dropdown[1] = False

    dropdowns = html.Div([

        html.Div([

                html.H6(
                    ['Eixo x:'], className='subtitle_style',
                ),

                dcc.Dropdown(
                    id = 'column-x',
                    options = [
                        {
                            'label': col,
                            'value': col,
                            'disabled': disabled_dropdown[0]
                        }
                        for col in series
                    ],
                    value = defaultx
                )
            ],
            style={'margin-left': '5px','width':'65%'}
        ),

        html.Div([

                html.H6(
                    ['Eixo y:'], className='subtitle_style',
                ),

                dcc.Dropdown(
                    id='column-y',
                    options=[
                        {
                            'label': col,
                            'value': col,
                            'disabled': disabled_dropdown[1]
                        }
                        for col in series
                    ],
                    value = None if app.dict_apps['app_dashboard_v01']['user_data_graph']['col-y'] is None \
                        else app.dict_apps['app_dashboard_v01']['user_data_graph']['col-y'],
                    multi = True
                )
            ],
            style={'margin-left': '5px','width':'65%'}
        ),
    ])

    graph_position = dcc.Graph(id='indicator-graphic')

    return dropdowns,graph_position 

def gera_grafico(col_x,list_coly,tipograf,df):

    fig = go.Figure()

    fig.update_layout(
        height=500,
        hovermode='x',
        legend = dict(
            orientation="h",
            yanchor = "bottom",
            y = 1,
            xanchor = "right",
            x = 1,
        )
    )
    
    fig.update_xaxes(title=col_x)

    fig.update_yaxes(
        title=str(list_coly).strip('[]') if len(list_coly) <=3 else str(list_coly[:4]).strip('[]') + '...'
    )

    if tipograf =='Gráfico de Linha':
        gera_grafico_de_linha(col_x,list_coly,df,fig)

    elif tipograf =='Gráfico de Barra Agrupado':
        gera_grafico_de_barra_agrupado(col_x,list_coly,df,fig)

    elif tipograf =='Gráfico de Barra Empilhado':
        gera_grafico_de_barra_empilhado(col_x,list_coly,df,fig)
        
    elif tipograf =='Histograma':
        gera_grafico_histograma(list_coly,df,fig)

    elif tipograf =='Box Plot':
        gera_grafico_boxplot(list_coly,df,fig)
    else:
        return fig
    
    # É possível salvar as informações das dropdown eixo x, eixo y e tipo de gráfico, porém, com as opções salvas, não é possivel trocar de aba e retornar para a aba gráfico com a visualização do gráfico ainda disponivel
    # Assim, deixei como já estava nas versões anteriores, somente com as opções salvas

    return fig

def gera_grafico_de_linha(col_x,list_coly,df,fig):
    print(f'(gera_grafico_de_linha) df = {df.head()}')
    for variavel in list_coly:
        fig.add_trace(
            go.Scatter(
                x=df[col_x],
                y=df[variavel],
                name=variavel,
                visible=True,
                mode='lines+markers',
                cliponaxis=False,
                opacity=0.8
            )
        )

    fig.update_xaxes(
        rangeslider=dict(visible=True),
        type='date'
    )
        
    return fig

def gera_grafico_de_barra_agrupado(col_x,list_coly,df,fig):

    for variavel in list_coly:
        fig.add_bar(
            x=df[col_x],
            y=df[variavel],
            name=variavel,
            opacity=0.8
        )

    fig.update_layout(
        barmode='group',
        bargroupgap=0.05
    )

    fig.update_xaxes(
        rangeslider=dict(visible=True),
        type='date'
    )

    return fig

def gera_grafico_de_barra_empilhado(col_x,list_coly,df,fig):

    range_eixo_y = []

    for variavel in list_coly:
        fig.add_bar(
            x=df[col_x],
            y=df[variavel],
            name=variavel,
            opacity=0.8
            )
        range_eixo_y.append(max(df[variavel]))
    
    escala_eixo_y = (sum(int(val) for val in range_eixo_y))*1.3 if list_coly != None else 100
    
    fig.update_layout(
            barmode='stack',
            bargroupgap=0.05,
            yaxis=dict(
                range=[0,escala_eixo_y]
            )
        )

    fig.update_xaxes(
            rangeslider=dict(visible=True),
            type='date'
        )

    return fig

def gera_grafico_histograma(list_coly,df,fig):
    # histfunc e histnorm

    for variavel in list_coly:
        fig.add_trace(
            go.Histogram(
            x=df[variavel],
            name=variavel,
            visible=True,
            opacity=0.8
            )
        )

    fig.update_layout(barmode = 'overlay')

    fig.update_xaxes(type='linear')

    return fig

def gera_grafico_boxplot(list_coly,df,fig):

    for variavel in list_coly:
        fig.add_trace(
            go.Box(
            y=df[variavel],
            name=variavel,
            visible=True,
            opacity=0.8
            )
        )
    fig.update_traces(boxpoints='all', jitter=0)
    fig.update_xaxes(type='linear')

    return fig


# Callbacks


@app.callback(
    [
        Output('options-dropdown-column','children'),
        Output('graph-position','children')
    ],
    [
        Input('type-graf','value')
    ]
)
def update_layout(tipograf):

    df = app.dict_apps['app_dashboard_v01']['series_df']
    app.dict_apps['app_dashboard_v01']['user_data_graph']['tipo'] = tipograf

    return gera_dropdowns_columns(tipograf,df)


@app.callback(
    Output('indicator-graphic','figure'),
    [
        Input('column-x','value'),
        Input('column-y','value'),
    ]
)
def update_grafico(col_x,list_coly):

    df = app.dict_apps['app_dashboard_v01']['series_df']
    print(f'(update_grafico) df = {df.head()}')

    tipograf = app.dict_apps['app_dashboard_v01']['user_data_graph']['tipo']

    if list_coly is None and app.dict_apps['app_dashboard_v01']['user_data_graph']['col-y'] != None:
        list_coly = app.dict_apps['app_dashboard_v01']['user_data_graph']['col-y']
    else:
        app.dict_apps['app_dashboard_v01']['user_data_graph']['col-y'] = list_coly

    if col_x is None and tipograf not in ['Histograma','Box Plot'] or list_coly is None:
        col_x = app.dict_apps['app_dashboard_v01']['user_data_graph']['col-x']
        return go.Figure()
    else:
        app.dict_apps['app_dashboard_v01']['user_data_graph']['col-x'] = col_x
        return gera_grafico(
                        col_x,
                        list_coly,
                        tipograf,
                        df
                )