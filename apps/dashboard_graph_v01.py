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

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def gera_layout():

    tipos_graf = [
        'Gráfico de Linha',
        'Gráfico de Barra Agrupado',
        'Gráfico de Barra Empilhado',
        'Histograma',
        'Box Plot',
    ]
            
    return html.Div(
        [
            html.H2(
                ['Gráfico das Series'], className='title_style',
            ),

            html.Hr(className='hr'),

            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                ['Visualização:'],
                                className='subtitle_style',
                            ),

                            dcc.Dropdown(
                                id='type-graph',
                                options=[
                                    {
                                        'label': tipo,
                                        'value': tipo,
                                    }
                                    for tipo in tipos_graf
                                ],
                                className='dropdowns_style',
                                value = tipos_graf[0],
                                # value = app.dict_apps['app_dashboard_v01']['user_data_graph']['tipo'],
                                clearable = False,
                                persistence = True,
                                persistence_type = 'memory',
                            )
                        ],
                        style={'margin-left': '5px','width':'65%','height':'100px'}
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
        ],
        style={'margin-left':'20px','margin-right':'20px','height':'630px'}
    )

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

    dropdowns = html.Div(
        [
            html.Div(
                [
                    html.Label(
                        ['Eixo x:'],
                        className='subtitle_style',
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
                        className='dropdowns_style',
                        value = defaultx,
                        clearable = False,
                        persistence = True,
                        persistence_type = 'memory',
                    )
                ],
                style={'margin-left': '5px','width':'65%','height':'90px'}
            ),

            html.Div(
                [
                    html.Label(
                        ['Eixo y:'],
                        className='subtitle_style',
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
                        className='dropdowns_style',
                        value = None,
                        multi = True,
                        clearable = True,
                        persistence = True,
                        persistence_type = 'memory',
                    )
                ],
                style={'margin-left': '5px','width':'65%','height':'90px'}
            ),
        ]
    )

    graph_position = dcc.Graph(
        id='indicator-graphic',
        config=dict(
            displayModeBar=False,
            scrollZoom=True
        ),
    )

    return dropdowns,graph_position 

def gera_grafico(col_x,list_coly,tipograf,df):

    fig = go.Figure()

    fig.update_layout(
        height=500,
        uirevision='foo',
        hovermode='x',
        showlegend= True,
        legend = dict(
            orientation="h",
            yanchor = "bottom",
            y = 1,
            xanchor = "right",
            x = 1,
            font=dict(
                color="#fff"
            ),
        ),
        plot_bgcolor= '#082255',
        paper_bgcolor='#082255',
        font_color= '#fff',
        margin = {
            "r":5,
            "t":5,
            "l":5,
            "b":5
        },
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

    return fig

def gera_grafico_de_linha(col_x,list_coly,df,fig):

    for variavel in list_coly:
        fig.add_trace(
            go.Scatter(
                x=df[col_x],
                y=df[variavel],
                name=variavel,
                visible=True,
                mode='lines+markers',
                cliponaxis=False,
                opacity=0.8,
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
            ybins=dict(
                    start=0,
                    # end=4,
                    # size=0.5
            ),
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

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++ CALLBACKS  ++++++++++++++++

@app.callback(
    [
        Output('options-dropdown-column','children'),
        Output('graph-position','children')
    ],
    [
        Input('type-graph','value')
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
        Input('type-graph','value')
    ]
)
def update_grafico(col_x,list_coly,tipograph):

    df = app.dict_apps['app_dashboard_v01']['series_df']

    if col_x is None and tipograph not in ['Histograma','Box Plot'] or list_coly is None:
        col_x = app.dict_apps['app_dashboard_v01']['user_data_graph']['col-x']
        return go.Figure()

    else:
        app.dict_apps['app_dashboard_v01']['user_data_graph']['col-x'] = col_x
        return gera_grafico(
                        col_x,
                        list_coly,
                        tipograph,
                        df
                    )