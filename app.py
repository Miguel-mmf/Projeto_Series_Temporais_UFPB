import dash

app = dash.Dash(
    __name__,
    title='Laboratório Web (st-mm)',
    update_title="Updating...", # default
    meta_tags=[
        {
            'name':'pst',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ],
    # suprimindo as exceções das callbacks para que caso utilize modificações dinâmicas do layout, não ocorra erros
    suppress_callback_exceptions=True
)

# app.config.suppress_callback_exceptions = True

server = app.server

# dicionário auxiliar
app.dict_apps = {}