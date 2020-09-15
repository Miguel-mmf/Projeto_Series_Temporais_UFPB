import dash_core_components as dcc
import dash_html_components as html
import dash_table

from dash_table.Format import Format, Scheme, Sign, Symbol
from app import app

def init_user_data():
    return {
        'file': {
            'test':None,
            'filename':'Nenhum Arquivo!',
            'filename_type':'Nenhuma Extensão de Arquivo!',
            'last_modified': None
        },
        'info_df': None,
    }

def gera_infor():

    df = app.dict_apps['app_dashboard_v01']['user_data_infor']['infor_df']

    return html.Div([

        dash_table.DataTable(
            
                data = df.to_dict('records'),

                columns = [
                    {
                        'name': col, 
                        'id': col,
                        'type': 'numeric',
                        'format': Format(precision=2, scheme=Scheme.fixed),
                    }
                    for col in df.columns
                ],

                style_cell={
                    'textAlign': 'center',
                    'border': '1px solid grey',
                    'minWidth':'90px',
                    'width':'125px',
                    'maxWidth':'160px',
                    'fontSize':'14',
                    'font-family':'sans-serif'
                    },
                
                style_header={
                    'backgroundColor': '#ADD8E6',
                    'fontWeight': 'bold'
                },

                # Anexando a coluna com o título de cada linha, faz mais sentido deixar a primeira coluna fixa.
                fixed_columns={'headers': True,
                            'data': 1},

                style_table={'height':'100%','minWidth': '100%','overflowX': 'auto'}
            )
        ],
        style={'margin-left':'15px'}
    )

def gera_layout():

    if app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['test'] == 'inserted':
        
        return html.Div([

            html.H2(
                ['Informações do Arquivo'], className='title_style',
            ),

            html.Hr(className='hr'),
            
            html.H4(
                ['Informações Gerais do Arquivo'], className='subtitle_style',
            ),

            dcc.Markdown(
                '###### **Nome do Arquivo:** {0}\n ###### **Tipo do Arquivo:** {1}\n ###### **Última Modificação:** {2}\n' 
                .format(
                    app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['filename'],
                    app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['filename_type'],
                    app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['last_modified']
                ),
                style={'margin-left':'15px'}
            ),
            
            html.Hr(className='hr'),

            html.H4(
                ['Informações Específicas do Arquivo'], className='subtitle_style',
            ),

            html.H6(
                ['Medidas de Tendência Central dos Dados:'], style={'font-weight': 'bold','margin-left':'15px'}
            ),

            gera_infor(),

            dcc.Markdown(
                '###### **Quantidade de Series:** {0}\n'
                .format(
                    str(
                        len(app.dict_apps['app_dashboard_v01']['series_df'].keys())
                    ),
                ),
                style={'margin-left':'15px'}
            ),         

        ])

    else:
        return html.Div([])

# Callbacks