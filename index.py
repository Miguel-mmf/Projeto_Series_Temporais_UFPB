# Lembrete: 
# Para gerar o arquivo environment.yml, use o comando:
# conda env export > environment.yml
# com venvst ativado.

# Usei instruções desse site:
# https://elements.heroku.com/buildpacks/conda/conda-buildpack
# para adicionar um buildpack de python-conda. A URL é
# https://github.com/conda/conda-buildpack.git
# Forneci essa url no dashboard do projeto, aba settings.

# Tentei com o buildpack, mas deu erro:
#
# -----> Python/Conda app detected
# -----> Preparing Python/Miniconda Environment (3.8.3)
# /tmp/codon/tmp/buildpacks/298b2b29cc393b8d85322805d763db20318c981c/bin/steps/conda_compile: line 9: conda: command not found
#  !     Push rejected, failed to compile Python/Conda app.
#  !     Push failed
#
# Coloquei o buildpack de python e adicionei novamente o requirements.txt.
#
#        Collecting MarkupSafe==1.1.1
#          Downloading MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl (27 kB)
#        ERROR: Could not find a version that satisfies the requirement mkl-fft==1.1.0 (from -r /tmp/build_644933f8_/requirements.txt (line 17)) (from versions: 1.0.0.17, 1.0.2, 1.0.6)
#        ERROR: No matching distribution found for mkl-fft==1.1.0 (from -r /tmp/build_644933f8_/requirements.txt (line 17))
#  !     Push rejected, failed to compile Python app.
#  !     Push failed

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app_descricao_v01
from apps import app_dashboard_v01

def gera_layout():

    return html.Div([

        html.H1('Laboratório de Séries Temporais', className='title_style'),
        html.P('Página Principal - DEE/CEAR/UFPB', className='title_style'),

        html.Hr(className='hr'),

        html.P('Versão 0.1 - junho/julho 2020', className='subtitle_style'),
        
        html.Div([

            dcc.Link('Descrição',
                href='/apps/v01/descricao',
                className='button button_link_style',
            )
        ]),

        html.Div([

            dcc.Link('Dashboard',
                href='/apps/v01/dashboard',
                className='button button_link_style',
            )
        ]),

        html.Hr(className='hr'),
        
    ],style={
        'margin-left':'15px',
        'margin-right':'15px'
    })

# Inicializa a variável server (foi necessária para heroku funcionar)
server = app.server

app.layout = html.Div([
    dcc.Location(
        id='url',
        refresh=False
    ),
    html.Div(
        id='page-content',
        children=gera_layout()
    ),
])

# Callbacks

@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname')
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
    app.run_server(debug=False)