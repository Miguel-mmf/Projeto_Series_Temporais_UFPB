import dash_core_components as dcc
import dash_html_components as html

from app import app
from apps import apoio_layout


if 'app_descricao_v01' not in app.dict_apps:
    app.dict_apps['app_descricao_v01'] = {}


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                              Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def gera_layout():
    # *** Me permite inserir uma linha horizontal da mesma forma quando é utilizado html.Hr() assim como ___
        
    return html.Div(
        [
            # header
            html.Div(
                [
                    html.H1(
                        'Descrição',
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
                    html.H3(
                        'Projeto Series Temporais',
                        className='subtitle_style',
                        style={'margin-left':'70px',}
                    ),

                    dcc.Markdown('''

        #### **Objetivos** 

        O objetivo desse projeto é criar um laboratório web para manipulação de séries temporais.  
        
        &nbsp
        
        #### **Metodologia**

        O desenvolvimento será feito remotamente por meio de desafios semanais.\n
        Uma reunião semanal para discussão sempre às sextas-feiras, 14hs.\n
        O código desenvolvido é enviado sempre na véspera, para que o professor tenha tempo de ver e se preparar para a reunião.\n
        Na reunião, o aluno apresenta o que fez e as dificuldades encontradas. O professor tenta ajudar nas dificuldades ou mostrar uma \
        forma alternativa de fazer e então, é apresentada a meta da semana seguinte e repete o processo. 

        &nbsp

        #### **Materiais**

        * Linguagem de programação Python
        * Biblioteca Dash:
            * [Plotly | Dash](https://dash.plotly.com/)
            * [Structuring a Multi-Page App](https://dash.plotly.com/urls)
            * [Upload Component](https://dash.plotly.com/dash-core-components/upload)
            * [dcc.Markdown](https://dash.plotly.com/dash-core-components/markdown)

        &nbsp

        #### **Desafio da semana 7 (03-07/08/2020):**

        * Modificações no arquivo `app.py`:
            * Foi criado um novo dicionário chamado de `app.dict_style_apps` uma vez que muitos componentes utilizavam um mesmo *style*. Isso como forma de deixar tudo organizado dentro de um dicionário contendo somente esses styles para ser mais fácil de modificar posteriormente;
        * Modificações no arquivo `app_dashboard_v01,py`:
            * Os testes utilizados para solucionar o problema de inserir outro arquivo com um arquivojá carregado anteriormente permaneceram;
            * O `df` da callback `update_tabs_content(tab)` e foi retirado e deixado dentro de cada arquivo infor, table e graph;
            * O teste para que não retorne nada em tabs-content, pois retirei o `df` da call-back `update_tabs_content(tab)`:
            ```py
                if(app.dict_apps['app_dashboard_v01'][''user_data_infor']['file']['test'] is None):
                    return html.Div([])
            ```
        * Modificações no arquivo `dashboard_infor_v01.py`:
            * O dicionário `app.dict_apps'['app_dashboard_v01']['user_data_infor']'` carrega as seguintes chaves:
                * `file`;
                * `infor_df`.
        * Modificações no arquivo `dashboard_graph_v01.py`:
            * A escala do eixo y foi configurada de forma que ela compreenda o intervalo `[0,`escala_eixo_y`]` uma vez que \
            `escala_eixo_y` é a soma do maior valor de cada serie inserida, como estava na versão da semana passada, só que \
            multiplicada por 1.3 para que exista uma melhor visualização do gráfico.

        &nbsp

        #### **Desafio da semana 6 (27-31/07/2020):**

        * Organizar a tabela na aba Informações deixando a descrição do que cada linha significa (contagem, média...).
        * Estudar uma melhor forma para apresentar a tabela na aba Tabela.
        * Organizar a página inicial e estudar a viabilidade da propriedade (className) do componente dcc.link() para ser utilizada.
        * Modificações no arquivo `index.py`:
            * A propriedade style para deixar o botão uniforme para cada opção;
            * Separação do código pois tinha muito código junto.
        * Modificações no arquivo app_dashboard_v01.py:
            * Foi inserida no dicionário `app.dict_apps['app_dashboard_v01']` uma chave chamada graph contendo um \
            dicionário para auxiliar na aba gráficos;
            * No dicionário `app.dict_apps['app_dashboard_v01']['graph']`, na chave `col-y`, o valor é retirado \
            dela sendo atribuido o valor `None` para evitar que dados de um segundo arquivo inserido some com as informações \
            do primeiro. Essa chave me auxilia na aba gráficos;
            * No dicionário `app.dict_apps['app_dashboard_v01']['infor_df']` foi criada a função `index_description(df)` \
            para fazer a troca da primeira coluna e renomear essa, inicialmente chamada de index, passando a ser "Descrição".
        * Modificações no arquivo `dashboard_infor_v01.py`:
            * A coluna 'Descrição' está fixada;
        * Modificações no arquivo `dashboard_table_v01.py`:
            * Está comentada a propriedades que deixavam o cabeçalho das colunas fixos e a propriedade que fixava as colunas;
        * Modificações no arquivo `dashboard_graph_v01.py`:
            * Uma função para cada gráfico com o tipo no nome de cada uma delas;
            * Para solucionar o problema de quando o tipo de gráfico escolhido fosse Histograma ou Box Plot, foi criada a função `gera_layout(df)` utilizada uma callback que retorna as dropdowns e o gráfico plotado;
            * Quando o tipo de gráfico escolhido for Histograma ou Box Plot, a dropdown do eixo x terá suas opções desativadas;
            * Retirando o tipo de gráfico, a dropdown de cada eixo têm suas opções desativadas e as opções, anteriormente escolhidas, sejam perdidas;
            * Na função `gera_gráfico()` a única modificação feita foi em `fig.update_yaxes`, em que foi criado um limite de títulos \
            para serem exibidos no gráfico (evitar a poluição do gráfico com os títulos dos eixos);
            * `app.dict_apps['app_dashboard_v01']['graph']['col-y']` serve para quando for realizada a troca de gráfico, ou seja, os valores \
            do eixo y não sejam perdidos e não seja necessário inserir essas informações a cada vez que mudar o tipo de gráfico;

        &nbsp

        #### **Desafio da semana 5 (13-17/07/2020):**

        * Uma nova tab chamada Informações em que será visualizada algumas informações do arquivo inserido.
            * Esaa tab está divida em informações específicas e gerais.
            * Novo dicionário chamado dashboard_infor_v01.
            * Nas informações especificas, retornar as medidas de tendência central dos dados.
        * Limpeza do código do arquivo `dashboard_graph_v01.py` e incremento com alguns elementos como:
            * O painel de manipulação do gráfico do lado esquerdo e o gráfico ao lado direito.
            * Uma opção para visualizar a escala do eixo x de forma linear ou temporal/datas.
            * Solução do problema do gráfico de barra empilhado foi solucionado com um limite de valor no eixo y.
            * Dois novos tipos de gráficos, histograma e Box Plot.
        * Para a aba tabela foram adicionadas as sugestões de que a tabela tenha uma barra de rolagem horizontal e uma largura fixa para as colunas. Além disso, foram feitas as seguintes modificações:
            * Opção de o usuário fixar até 3 colunas para que auxilie na comparação de valores entre colunas da tabela.
            * Quando não tem alguma coluna fixa, a tabela será exibida com o nome de cada coluna fixo em relação aos dados.
            * A paginação foi retirada uma vez que, para mim, a visualização ficou melhor quando é possível analisar a tabela com a ajuda das barras de rolagem vertical e horizontal.
            * Aumentei a fonte da tabela.
        * As modificações feitas no arquivo app_dashboard_v01.py serviram somente para auxiliar nas abas informações, tabela e gráficos.

        &nbsp

        #### **Desafio da semana 4 (06-10/07/2020):**

        * Simplificar a página Descrição, usando ‘___’ para inserir linha horizontal diretamente no markdown.
        * Mover os dados do arquivo carregado para uma aba auxiliar (3° tab), que pode ser chamada de Informações.
        * Separar o código de Dashboard em arquivos menores: Informações, Tabelas e Gráficos.
        * Na tab Gráficos, incluir uma 3° Dropdown na qual o usuário possa selecionar o tipo de gráfico que deseja ver: linha ou barras.
       
        &nbsp

        #### **Desafio da semana 3 (22-26/06/2020):**

        * Estudar a possibilidade de registrar o arquivo a partir da divisão do dataframe armazenando as series que o formam \
        dentro de um dicionário `app.dict_apps['app_dashboard_v01']={}`.
        * Utilizar endswith() para identificar o tipo de arquivo inserido.
        * Rever a página app_descricao_v01 e inserir o as atividades desenvolvidas nos desafios semanais \
        com [dcc.Markdown](https://dash.plotly.com/dash-core-components/markdown).

        &nbsp

        #### **Desafio da semana 2 (15-19/06/2020):**

        * Fatiar o código desenvolvido no primeiro desafio utilizando a estrutura de cada elemento em um arquivo separado \
        (facilitar a manutenção do código).
        * Estudar o código que está na seção [Upload Component](https://dash.plotly.com/dash-core-components/upload) e \
        tentar aplicar.   
        
        &nbsp

        #### **Desafio da semana 1 (8-12/06/2020):**

        * Criar o projeto que está na forma de instruções na seção [Structuring a Multi-Page App](https://dash.plotly.com/urls).
        * Depois que esse projeto de exemplo estiver funcionando, adaptar para uma página principal do tipo:
        ''',
            style={'margin-left':'20px','margin-right':'20px'}
                    ),

                    # Essas divs fazem parte do texto da semana 1.
                    html.Div(
                        [
                            html.H6('Laboratório de Series Temporais'),
                            html.H6('CEAR/UFPB')
                        ],
                        style={
                            'textAlign':'center',
                            'border': '2px solid lightgray',
                            'border-radius': '7px',
                            'height':'80px'
                        }
                    ),

                    html.Div(
                        [
                            html.H6(
                                'Página Principal / Descrição / Dashboard',
                                style={'lineHeight':'150px'}
                            ),
                        ],
                        style={
                            'textAlign':'center',
                            'border': '2px solid lightgray',
                            'border-radius': '7px',
                            'height':'150px',
                            'margin-top':'5px'
                        }
                    ),
                ],
                className='wind__speed__container',
                style={'height':'3800px'}
            ),

            # retornar para a página principal
            html.Div(
                apoio_layout.gera_button_return()
            ),

            # Rodapé
            apoio_layout.gera_rodape(),
        ],
    )

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++