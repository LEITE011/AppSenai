import asyncio

import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight, View
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



    # Gerenciar as Telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeiro Pagina",
                        bgcolor=Colors.AMBER_200,
                    ),
                    flet.Button("Ir Para Segunda Tela", on_click= lambda: navegar("/segunda_tela"))

                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Segunda Pagina",
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

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)
