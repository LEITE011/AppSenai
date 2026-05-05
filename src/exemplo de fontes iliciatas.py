import asyncio

import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight, View, FloatingActionButton, Icons, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, dropdown


# ================== CLASSE PESSOA ==================
class Pessoa:
    def __init__(self, nome: str, profissao: str, sexo: str):
        self.nome = nome
        self.profissao = profissao
        self.sexo = sexo  # "Masculino" ou "Feminino"

    @property
    def icone(self):
        """Retorna o ícone de acordo com o sexo"""
        if self.sexo == "Masculino":
            return Icons.MAN
        elif self.sexo == "Feminino":
            return Icons.WOMAN
        else:
            return Icons.PERSON

    def __str__(self):
        return f"{self.nome} - {self.profissao} ({self.sexo})"


# ================== CONFIGURAÇÕES ==================
def main(page: flet.Page):
    page.title = "Exemplo de Listas"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []  # Lista de objetos Pessoa

    # ================== FUNÇÕES ==================
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(Text(str(item)))

    def montar_lista_card():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                Card(
                    content=Row([
                            Icon(item.icone),
                            Text(str(item))
                        ],
                        margin=8,
                    ),
                )
            )

    def montar_lista_padrao():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(item.icone),  # Ícone dinâmico conforme sexo
                    title=Text(item.nome),
                    subtitle=Text(f"{item.profissao} ({item.sexo})"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icons.REMOVE_RED_EYE),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda i=item: excluir(i)),
                        ]
                    ),
                )
            )

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def limpar_campos():
        input_nome.value = ""
        input_profissao.value = ""
        input_sexo.value = None
        input_nome.error = None
        input_profissao.error = None

    def salvar_dados():
        nome = input_nome.value.strip()
        profissao = input_profissao.value.strip()
        sexo = input_sexo.value  # valor do Dropdown

        # Validações
        valido = True
        if not nome:
            input_nome.error = "Campo Obrigatório"
            valido = False
        else:
            input_nome.error = None

        if not profissao:
            input_profissao.error = "Campo Obrigatório"
            valido = False
        else:
            input_profissao.error = None

        if not sexo:
            valido = False

        if valido:
            # Cria objeto Pessoa e adiciona à lista
            pessoa = Pessoa(nome=nome, profissao=profissao, sexo=sexo)
            lista_dados.append(pessoa)
            limpar_campos()

        # Atualiza as telas
        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()

    # ================== GERENCIAR ROTAS ==================
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Exemplo de Listas"),
                        bgcolor=Colors.AMBER_200,
                    ),
                    flet.Button("Lista de Texto", on_click=lambda: navegar("/lista_texto")),
                    flet.Button("Lista de Card", on_click=lambda: navegar("/lista_card")),
                    flet.Button("Lista padrão Android", on_click=lambda: navegar("/lista_padrao")),
                ]
            )
        )

        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        flet.AppBar(title="Lista de Texto"),
                        input_nome,
                        input_profissao,
                        input_sexo,
                        btn_salvar,
                        list_view,
                    ]
                )
            )
        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        flet.AppBar(title="Lista de Card"),
                        input_nome,
                        input_profissao,
                        input_sexo,
                        btn_salvar,
                        list_view,
                    ]
                )
            )
        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(title="Lista padrão Android"),
                        list_view,
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda: navegar("/form_cadastro"),
                    ),
                )
            )
        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(title="Cadastro"),
                        input_nome,
                        input_profissao,
                        input_sexo,
                        btn_salvar,
                    ]
                )
            )

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # ================== COMPONENTES ==================
    input_nome = TextField(label="Nome", hint_text="Digite seu Nome", on_submit=salvar_dados)
    input_profissao = TextField(label="Profissão", hint_text="Digite sua Profissão", on_submit=salvar_dados)
    input_sexo = Dropdown(
        label="Sexo",
        hint_text="Selecione o Sexo",
        options=[
            dropdown.Option("Masculino"),
            dropdown.Option("Feminino"),
        ],
    )
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    # ================== EVENTOS ==================
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)