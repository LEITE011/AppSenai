import asyncio
from cProfile import label

import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight, View, FloatingActionButton, Icons, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, DropdownOption
from flet.controls import page, colors
from flet.controls.border_radius import horizontal
from datetime import datetime

from flet.controls.core.canvas import Color
from flet.controls.material import icons
from markdown_it.rules_block import lheading


class Pessoa:
    def __init__(self, nome, raca, genero, preco, tamanho, cor):
        self.nome = nome
        self.raca = raca
        self.genero = genero
        self.preco = preco
        self.tamanho = tamanho
        self.cor = cor


# Configurações
def main(page: flet.Page):
    # Configuraçoes
    page.title = "Exemplo de Listas"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode.light
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )

    def montar_lista_card():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Card(
                    content=Row([
                        Icon(Icons.PERSON),
                        Text(item.nome),
                        Text(item.raca)
                    ],
                        margin=8,
                    ),
                )
            )

    def montar_lista_padrao():
        list_view.controls.clear()

        # meu item é uma pessoa com nome, raca e genero
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.MALE) if item.genero == "Macho" else Icon(Icons.FEMALE),
                    title=(f"O Nome do Cachorro é {item.nome}"),
                    subtitle=(f"A Raça do Cachorro é {item.raca}"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, pessoa=item: ver_detalhes(pessoa)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )
    def ver_detalhes(pessoa):
        text_nome.value = pessoa.nome
        text_raca.value = pessoa.raca
        text_genero.value = pessoa.genero
        text_preco.value = pessoa.preco
        text_tamanho.value = pessoa.tamanho
        text_cor.value = pessoa.cor

        navegar("/detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value
        raca = input_raca.value
        genero = input_genero.value
        preco = input_preco.value
        tamanho = input_tamanho.value
        cor = input_cor.value

        tem_error = False
        if nome:
            input_nome.error = None
        else:
            tem_error = True
            input_nome.error = "campo obrigatorio"

        if raca:
            input_raca.error = None
        else:
            tem_error = True
            input_raca.error = "campo obrigatorio"

        if genero:
            input_genero.error = None
        else:
            tem_error = True
            input_genero.error = "campo obrigatorio"

        if genero:
            input_preco.error = None
        else:
            tem_error = True
            input_preco.error = "campo obrigatorio"

        if genero:
            input_tamanho.error = None
        else:
            tem_error = True
            input_tamanho.error = "campo obrigatorio"

        if genero:
            input_cor.error = None
        else:
            tem_error = True
            input_cor.error = "campo obrigatorio"

        if not tem_error:
            # montar objeto
            pessoa = Pessoa(
                nome=nome,
                raca=raca,
                genero=genero,
                preco=preco,
                tamanho=tamanho,
                cor=cor,
            )
            lista_dados.append(pessoa)

            input_nome.value = ""
            input_raca.value = ""
            input_genero.value = ""
            input_preco.value = ""
            input_tamanho.value = ""
            input_cor.value = ""
            navegar("/lista_padrao")

        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()

    # Gerenciar as Telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    flet.AppBar(
                        title="Lista padrão Android",
                    ),
                    list_view

                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )

        if page.route == "/form_cadastro":
            page.views.append(

                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="cadastro",
                        ),
                        input_nome,
                        input_raca,
                        input_preco,
                        input_tamanho,
                        input_cor,
                        input_genero,
                        btn_salvar,

                    ]
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                        ),
                        Container(
                            Column([
                                text_nome,
                                Row([
                                    Icon(Icons.DRIVE_FILE_RENAME_OUTLINE, color=Colors.PRIMARY, size=20),
                                    text_raca
                                ]),
                                Row([
                                    Icon(Icons.COLOR_LENS_OUTLINED, color=Colors.PRIMARY, size=20),
                                    text_cor
                                ]),
                                Row([
                                    Icon(Icons.FORMAT_SIZE_OUTLINED, color=Colors.PRIMARY, size=20),
                                    text_tamanho
                                ]),
                                Row([
                                    Icon(Icons.TRANSGENDER, color=Colors.PRIMARY, size=20),
                                    text_genero
                                ]),
                                Row([
                                    Icon(Icons.ATTACH_MONEY, color=Colors.PRIMARY, size=20),
                                    text_preco
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                            bgcolor=Colors.BLUE_700,
                            padding=15,
                            border_radius=10,
                            width=400
                        )
                    ]
                )
            )
            # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_nome = TextField(label="Nome", hint_text="Digite o Nome do Cachorro")
    input_raca = TextField(label="Raça", hint_text="Digite a Raça do Cachorro")
    input_preco = TextField(label="Preço", hint_text="Digite o Preço do Cachorro")
    input_tamanho = TextField(label="Tamanho", hint_text="Digite o Tamanho do Cachorro")
    input_cor = TextField(label="Cor", hint_text="Digite a Cor do Cachorro")
    input_genero = Dropdown(
        label="genero",
        hint_text="Selecione o Genero do Cachorro",
        options=[
            DropdownOption("Macho"),
            DropdownOption("Femea"),
        ],
    )
    btn_salvar = Button("salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    text_nome = Text(weight=FontWeight.BOLD, size=24)
    text_raca = Text()
    text_genero = Text()
    text_preco = Text()
    text_tamanho = Text()
    text_cor = Text()

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
