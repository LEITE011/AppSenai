import asyncio
from cProfile import label

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, Button
from datetime import datetime

from flet.controls import page


def main(page: flet.Page):

    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text.value = f"Olá {input_nome.value}, tudo bem?"
        input_nome.value = ""
        navegar("/msg")

        # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira página",
                        bgcolor=Colors.BLUE_700,



                    ),
                    input_nome,
                    bnt_nome
                ]
            )
        )
        if page.route == "/msg":
            page.views.append(
                View(
                    route="/msg",
                    controls=[
                        flet.AppBar(
                            title="Segunda página",
                            bgcolor=Colors.BLUE_700,
                        ),
                        text
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
    text = Text("")
    input_nome = TextField(label="Digite seu Nome: ")
    bnt_nome = OutlinedButton("Salvar", on_click=salvar_nome)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)
