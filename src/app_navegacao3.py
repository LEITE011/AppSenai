import asyncio

import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight, View, Row, Icon, Icons
from flet.controls import page, colors
from flet.controls.border_radius import horizontal
from datetime import datetime

from flet.controls.core.canvas import Color


# Configurações
def main(page: flet.Page):
    # Configuraçoes
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode.light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)

        )

    # Funções

    def exibir_informacoes():
        text_raca.value = f"raca: {input_raca.value}"
        text_cor.value = f"cor: {input_cor.value}"
        text_tamanho.value = f"tamanho: {input_tamanho.value}"
        text_genero.value = f"genero: {input_genero.value}"
        text_preco.value = f"preço: R${input_preco.value}"

        tem_error = False
        if input_raca.value:
            input_raca.error = None
        else:
            tem_error = True
            input_raca.error = "campo obrigatorio"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_error = True
            input_cor.error = "campo obrigatorio"

        if input_tamanho.value:
            input_tamanho.error = None
        else:
            tem_error = True
            input_tamanho.error = "campo obrigatorio"

        if input_genero.value:
            input_genero.error = None
        else:
            tem_error = True
            input_genero.error = "campo obrigatorio"

        if input_preco.value:
            input_preco.error = None
        else:
            tem_error = True
            input_preco.error = "campo obrigatorio"

        if not tem_error:
            input_raca.value = ""
            input_cor.value = ""
            input_tamanho.value = ""
            input_genero.value = ""
            input_preco.value = ""
            navegar("/tela_msg")

    # Gerenciar as Telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Cadastro de Funcionarios",
                        bgcolor=Colors.BLUE_700,
                    ),
                    Text("Digite as Informações a Seguir Para o Cadastro"),
                    input_raca,
                    input_cor,
                    input_tamanho,
                    input_genero,
                    input_preco,
                    btn_salvar

                ]
            )
        )
        if page.route == "/tela_msg":
            page.views.append(
                View(
                    route="/tela_msg",
                    controls=[
                        flet.AppBar(
                            title="Segunda Pagina",
                        ),
                        Container(
                            Column([
                                text_raca,
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
    text_raca = Text()
    input_raca = TextField(label="raca")
    text_cor = Text()
    input_cor = TextField(label="cor")
    text_tamanho = Text()
    input_tamanho = TextField(label="tamanho")
    text_genero = Text()
    input_genero = TextField(label="genero")
    text_preco = Text()
    input_preco = TextField(label="preço")
    btn_salvar = Button("Salvar", on_click=exibir_informacoes)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
