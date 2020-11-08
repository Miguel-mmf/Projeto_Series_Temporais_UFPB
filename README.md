<h1 align="center">Projeto Series Temporais 2020</h1>
**Link da Aplicação na Web:** [Projeto Series Temporais](https://pstemporais.herokuapp.com/)

O Projeto Series Temporais consiste na construção de um laboratório web para a manipulação de series temporais utilizando a Heroku, uma plataforma de hospedagem, testes e produção de aplicações web.

### **Metodologia**
O desenvolvimento será feito remotamente por meio de desafios semanais.

Uma reunião semanal para discussão sempre às sextas-feiras, 14hs.

O código desenvolvido é enviado sempre na véspera, para que o professor tenha tempo de ver e se preparar para a reunião.

Na reunião, o aluno apresenta o que fez e as dificuldades encontradas. O professor tenta ajudar nas dificuldades ou mostrar uma forma alternativa de fazer e então, é apresentada a meta da semana seguinte e repete o processo.

***

<h1 align="center">Rodando a aplicação localmente na sua máquina</h1>

Aconselho você a criar um ambiente virtual novo ou criar um a partir do meu arquivo `environment.yml` que carrega todas as informações do ambiente conda que utilizei para desenvolver esse trabalho.

#### **Criando o Ambiente através do arquivo `environment.yml`**

Com o seu prompt de comando aberto, execute

```
conda env create -f environment.yml
```

Para verificar se o ambiente foi criado corretamente, execute no seu terminal

```
conda env list
    ou
conda info --envs
```

#### **Instalando as dependências necessárias:**

Caso você já tenha um ambiente na sua máquina, é necessário verificar se as dependencias requeridas dentro do arquivo `requirements.txt` disponível acima já existe no seu ambiente. Caso não, ative o seu ambiente e execute

```

pip install -r requirements.txt
```

### **Clonando o repositório**

Com todos os pacotes necessários instalados, clone o repositório para sua máquina com

```
git clone [o link está disponível na opção **Code** na página principal do repositório]
```

#### **Rodando a aplicação**

Execulte a aplicação com

```
python index.py
```

***

### **Materiais**
* Linguagem de programação [Python](https://docs.python.org/3/)
* Biblioteca Dash:
    * [Plotly | Dash](https://dash.plotly.com/)
    * [Dash Core Components](https://dash.plotly.com/dash-core-components)
    * [Dash HTML Components](https://dash.plotly.com/dash-html-components)
    * [Dash DataTable](https://dash.plotly.com/datatable)
        * [Dash DataTable - Styling](https://dash.plotly.com/datatable/style).
        * [Dash DataTable - Interactivity](https://dash.plotly.com/datatable/interactivity).
        * [Editable DataTable](https://dash.plotly.com/datatable/editable).
    * [Dash Dev Tools](https://dash.plotly.com/devtools)
    * [Structuring a Multi-Page App](https://dash.plotly.com/urls)
    * [Upload Component](https://dash.plotly.com/dash-core-components/upload)
    * [dcc.Markdown](https://dash.plotly.com/dash-core-components/markdown)

### **Integrantes**
**Aluno:** Miguel Marques Ferreira

**Orientador:** Professor Helon David de Macedo Braz