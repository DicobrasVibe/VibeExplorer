import flet as ft
from AppOpener import open
import os


def main(page: ft.Page):    # функция страницы. её параметры и что в ней находится

    page.window_width = 900    # Ширина окна
    page.window_height = 600    # Высота окна

    page.bgcolor = "#2D033B"    # Цвет фона

    fileopener = ft.ElevatedButton(text="ярлык")    # Создание кнопки
    fileopener2 = ft.ElevatedButton(text="ярлык", width=100, bgcolor="#E5B8F4", color= "#810CA8")   # Добавляем ширину, фон, цвет текста

    page.add(fileopener)    # Добавление кнопки в окно
    page.add(fileopener2)


    FOp = ft.ElevatedButton(text="ярлык 1")
    FOp2 = ft.ElevatedButton(text="ярлык 2")

    lineFO = ft.Row(controls=[FOp, FOp2])   # Создание строки из элементов      # можно использовать alignment=ft.MainAxisAlignment.CENTER/END/SPASE_AROUND/etc для выравнивания

    funtext = ft.Text(value="Мяу)", color="GREY", size=25)

    page.add(lineFO, funtext)

    def opentxt(p):
        os.system("test.txt")


    Opener = ft.ElevatedButton(text="Открыть", on_click  =opentxt)
    page.add(Opener)


    
    page.navigation_bar = ft.NavigationBar(destinations=[ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon = ft.icons.BOOKMARK, label="Explore",),],)
    page.add(page.navigation_bar)





ft.app(target=main)     # Создание окна