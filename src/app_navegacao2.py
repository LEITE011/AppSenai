import asyncio

import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight, View, Icon, Row, Icons



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
        text_nome.value = f"Nome: {input_nome.value}"
        text_cpf.value = f"CPF: {input_cpf.value}"
        text_email.value = f"Email: {input_email.value}"
        text_salario.value = f"Salario: R${input_salario.value}"

        tem_error = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_error = True
            input_nome.error = "campo obrigatorio"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_error = True
            input_cpf.error = "campo obrigatorio"

        if input_email.value:
            input_email.error = None
        else:
            tem_error = True
            input_email.error = "campo obrigatorio"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_error = True
            input_salario.error = "campo obrigatorio"

        if not tem_error:
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,
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
                                text_nome,
                                Row([
                                    Icon(Icons.MAIL, color=Colors.PRIMARY, size=20),
                                    text_email
                                ]),
                                Row([
                                    Icon(Icons.CREDIT_CARD_OUTLINED, color=Colors.PRIMARY, size=20),
                                    text_cpf
                                ]),
                                Row([
                                    Icon(Icons.ATTACH_MONEY, color=Colors.PRIMARY, size=20),
                                    text_salario
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
    text_nome = Text()
    input_nome = TextField(label="Nome")
    text_cpf = Text()
    input_cpf = TextField(label="CPF")
    text_email = Text()
    input_email = TextField(label="Email")
    text_salario = Text()
    input_salario = TextField(label="Salario")
    text_nome = Text()
    btn_salvar = Button("Salvar", on_click=exibir_informacoes)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
