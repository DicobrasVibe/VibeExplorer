import flet as ft
from AppOpener import open
import os


def main(page: ft.Page):

    page.title = "Vibe Explorer"

    MainMenu = ft.ElevatedButton(text="Главная")
    TitleLine = ft.Row(controls=[MainMenu],alignment=ft.MainAxisAlignment.CENTER)
    page.add(TitleLine)

    # HSR = ft.ElevatedButton(content= "HSRico")
    # page.add(HSR)


ft.app(target=main)