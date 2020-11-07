import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from apps import app_descricao_v01
from apps import app_dashboard_v01
from apps import apoio_layout

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
                        'Laboratório de Séries Temporais',
                        className='title_style'
                    ),

                    html.H6(
                        'Página Principal - DEE/CEAR/UFPB',
                        className='title_style'
                    ),
                ],
                className='wind__speed__container',
                style={'height':'120px'}
            ),

            html.Div(
                [
                    html.P(
                        'Versão 0.1 - junho/julho 2020',
                        className='title_style',
                        style={'margin-top':'10px'}
                    ),
        
                    html.Div(
                        [
                            html.Label(
                                'Para acessar a página Descrição, selecione o botão abaixo:',
                                className='descricao_index_style'
                            ),

                            dcc.Link('Descrição',
                                href='/apps/v01/descricao',
                                className='button button_link_style',
                            )
                        ],
                        className='one-half column',
                    ),

                    html.Div(
                        [
                            html.Label(
                                'Para acessar a página Dashboard, selecione o botão abaixo:',
                                className='descricao_index_style'
                            ),

                            dcc.Link('Dashboard',
                                href='/apps/v01/dashboard',
                                className='button button_link_style',
                            )
                        ],
                        className='one-half column',
                    ),
                ],
                className='wind__speed__container',
                style={'height':'275px'}
            ),
        
            # logos (CEAR e UFPB)
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src= app.get_asset_url('image/logo_cear.png'),
                                title='Centro de Energias Alternativas e Renováveis (CEAR)',
                                alt='Centro de Energias Alternativas e Renováveis (CEAR)',
                                className='cear_ufpb',
                            )
                        ],
                        className='six columns box_cear_ufpb',
                    ),

                    html.Div(
                        [
                            html.Img(
                                src= app.get_asset_url('image/logo_ufpb.png'),
                                title='Universidade Federal da Paraíba (UFPB)',
                                alt='Universidade Federal da Paraíba (UFPB)',
                                className='cear_ufpb',
                            )
                        ],
                        className='six columns box_cear_ufpb',
                    ),
                ],
                style={'height':'225px'}
            ),

            # Rodapé
            apoio_layout.gera_rodape(),
        ]
    )

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++ LAYOUT  ++++++++++++++++

app.layout = html.Div(
    [
        dcc.Location(
            id='url',
            refresh=False
        ),

        html.Div(
            children = gera_layout(),
            id='page-content',
        ),
    ]
)

# ++++++++++++++++ CALLBACKS  ++++++++++++++++

@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname'),
    ]
)
def display_page(pathname):
    
    if pathname == '/':
        return gera_layout()
    elif pathname == '/apps/v01/descricao':
        return app_descricao_v01.gera_layout()
    elif pathname == '/apps/v01/dashboard':
        return app_dashboard_v01.gera_layout()
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)