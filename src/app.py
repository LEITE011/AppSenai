import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight
from flet.controls import page
from flet.controls.border_radius import horizontal
from datetime import datetime

from flet.controls.core.canvas import Color


def main(page: flet.Page):
    # Configuraçoes
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode.light
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        text.value = f"Bom Dia Meu Grande Rei {input_nome.value} {input_sobrenome.value}"
        page.update()

    # Componetes
    text = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    def verificar_par_inpar():
        numero2 = int(input_numero1.value)
        if numero2 % 2 == 0:
            texto = f'{numero2} o numero é par'
        else:
            texto = f'{numero2} o numero é impar'
        text.value = texto

    # Componetes
    text2 = Text()
    input_numero1 = TextField(label="Digite um Numero Par ou Impar Para a Verificação")
    btn_verificar = OutlinedButton("Verificar", on_click=verificar_par_inpar)

    def verificar_maior():
        menor_minimo = int(input_ano.value)
        maior_ou_menor = datetime.now().year - menor_minimo

        if maior_ou_menor >= 18:
            textoo = f'Se a Pessoa tem {menor_minimo} a pessoa é maior de Idade'

        else:
            textoo = f'Se a Pessoa tem {menor_minimo} a pessoa é menor de Idade'
        text.value = textoo

    # Componetes
    text3 = Text()
    input_ano = TextField(label="Digite o Ano de Nascimento da Pessoa")
    btn_ano = OutlinedButton("Verificar Ano", on_click=verificar_maior)

    # Construção da Tela

    page.add(
        Column(
            [
                Container(
                    Column(
                        [
                            Text("Atividade 1", weight=FontWeight.BOLD, size=24),
                            input_nome,
                            input_sobrenome,
                            btn_salvar,
                            text,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.BLUE_700,
                    padding=15,
                    border_radius=10,
                    width=400,

                ),

                Container(
                    Column(
                        [
                            Text("Atividade 2", weight=FontWeight.BOLD, size=24),
                            input_numero1,
                            btn_verificar,
                            text2,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.RED_700,
                    padding=15,
                    border_radius=10,
                    width=400,

                ),

                Container(
                    Column(
                        [
                            Text("Atividade 3", weight=FontWeight.BOLD, size=24),
                            input_ano,
                            btn_ano,
                            text3,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.GREEN_700,
                    padding=15,
                    border_radius=10,
                    width=400,

                ),

            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )


flet.run(main)
