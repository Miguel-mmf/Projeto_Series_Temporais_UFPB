import io
import base64
import datetime
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from apps import dashboard_infor_v01 as infor
from apps import dashboard_table_v01 as table
from apps import dashboard_graph_v01 as graph
from apps import apoio_layout


if 'app_dashboard_v01' not in app.dict_apps:
    app.dict_apps['app_dashboard_v01'] = {
        'series_df': None,
        'user_data_infor': infor.init_user_data(),
        'user_data_table': table.init_user_data(),
        'user_data_graph': graph.init_user_data(),
    }

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                              Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def gera_layout():
    
    return html.Div(
        [
            # header
            html.Div(
                [
                    html.H1(
                        'Dashboard',
                        className='title_style'
                    ),

                    html.H6(
                        'DEE/CEAR/UFPB',
                        className='title_style'
                    ),
                ],
                className='wind__speed__container',
                style={'height':'120px'}
            ),

            html.Div(
                [
                    dcc.Markdown('''

                        ##### **Visualização de Dados**

                        Após inserir o arquivo, é possível manipular as opções que surgirão abaixo e visualizar os dados inseridos por meio da descrição deles, da organização em tabela e da construção de gráficos.
                        ''',
                        style={'margin-left':'20px','margin-right':'20px'}
                    ),

                    dcc.Upload(
                        id='upload-data',
                        className='upload_box_style',
                        children=html.Div(
                            [
                                'Arraste e solte ou ', html.A('Escolha um arquivo...')
                            ]
                        ),
                    ),

                    html.Div(
                        id='output-data',
                        style={'margin-top':'20px','margin-left':'20px','margin-right':'20px'}
                    ),

                    html.H5(
                        ['Selecione a forma que você deseja visualizar o conteúdo do arquivo !'],
                        style={'textAlign':'center','margin-top':'20px','margin-left':'20px','margin-right':'20px'}
                    ),
                ],
                className='wind__speed__container',
                style={'height':'330px'}
            ),

            dcc.Tabs(
                id="tabs",
                # value='tab-1',
                # Esse value = 'tab-1' é default do componente.
                children=[
                    dcc.Tab(label='Informações', value='info-val',className='tab_hearder_style'),
                    dcc.Tab(label='Tabela', value='tabela-val',className='tab_hearder_style'),
                    dcc.Tab(label='Gráficos', value='grafico-val',className='tab_hearder_style'),
                ],
            ),

            html.Div(id='tabs-content'),

            # retornar para a página principal
            html.Div(
                apoio_layout.gera_button_return()
            ),

            # Rodapé
            apoio_layout.gera_rodape(),

        ],
    )

def index_description(df):

    df1 = df.describe().reset_index()
    df1.rename(columns={'index': 'Descrição'}, inplace=True)

    return df1

def parse_contents(contents, filename, date):
    
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    extension = filename.split(".")[-1]
    try:
        if extension in ['csv','txt','dat']:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            filename_type = extension
        elif extension in ['xls','xlsx']:
            df = pd.read_excel(io.BytesIO(decoded))
            filename_type = extension
        else:
            df = pd.DataFrame()
            filename_type = ''
    
    except Exception as e:
        print(e)
        return html.Div([
            html.H4('(parse_contents) Houve um erro de leitura!')
        ])
    
    print(f'(parse_contents) df = {df.head()}')
    app.dict_apps['app_dashboard_v01']['series_df'] = df

    app.dict_apps['app_dashboard_v01']['user_data_infor'] = {
        'file': {
            'test':'inserted',
            'filename':filename,
            'filename_type':filename_type,
            'last_modified':str(datetime.datetime.fromtimestamp(date))
        },
        'infor_df': index_description(df)
    }

    return html.Div(
        [
            html.H6('O arquivo {} está pronto para ser visualizado !'.format(filename))
        ])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++ CALLBACKS  ++++++++++++++++

@app.callback(
    Output('output-data', 'children'),
    [
        Input('upload-data', 'contents')
    ],
    [
        State('upload-data', 'filename'),
        State('upload-data', 'last_modified')
    ]
)
def update_output(content, name, date):

    # Atualiza o texto que aparece acima das Tabs informando se algum arquivo foi lido.

    if content is None:

        if app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['test']=='inserted':
            
            children = html.Div([

                html.H6('O arquivo {} ainda pode ser visualizado !\
                    Caso queira visualizar outro arquivo, é preciso apenas inseri-lo.'
                    .format(app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['filename']))
            ])
        else:
            children = [

                html.Div([
                    html.H6('Nenhum arquivo inserido. As extensões de arquivo aceitas são: \
                        .csv, .txt, .dat, .xls ou .xlsx')
                ])
            ]
    else:

        if name is not app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['filename']:
            app.dict_apps['app_dashboard_v01']['user_data_graph'] = graph.init_user_data()

        children = [
            parse_contents(
                content,
                name,
                date
            )
        ]
        
    return children


@app.callback(
    Output('tabs-content','children'),
    [
        Input('tabs','value')
    ]
)
def update_tabs_content(tab):

    # Atualiza o conteúdo do componente tabs, de acordo com os cliques do usuário.

    if(app.dict_apps['app_dashboard_v01']['user_data_infor']['file']['test'] is None):
        return html.Div(
            [],
            style={'height':'100px'}
        )

    # tab-1 é o valor default do componente. Nesse caso, retorna vazio!
    if tab == 'tab-1':
        return html.Div(
            [],
            style={'height':'100px'}
        )
    elif tab == 'info-val':
        return html.Div(
            [
                infor.gera_layout()
            ],
            className='wind__speed__container',
            style={'margin-top':'0px'}
        )
    elif tab == 'tabela-val':
        return html.Div(
            [
                table.gera_layout()
            ],
            className='wind__speed__container',
            style={'margin-top':'0px'}
        )
    elif tab == 'grafico-val':
        return html.Div(
            [
                graph.gera_layout()
            ],
            className='wind__speed__container',
            style={'margin-top':'0px'}
        )
    else:
        return html.Div(f'(update_tabs_content) Valor de tab inesperado (tab = {tab})!')