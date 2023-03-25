from tkinter import Menu

#from pages.PageEnums import PagesEnum
#from pages.PageSet01 import Page1, Page2, StartPage


class MainMenu(Menu):
    def __init__(self, parent):
        menubar = Menu(parent)
        parent.config(menu=menubar)

        # pages_menu = Menu(menubar, tearoff=False)
        # pages_menu.add_command(
        #     label=PagesEnum.StartPage.value,
        #     command=lambda: parent.show_frame(PagesEnum.StartPage)
        # )
        # pages_menu.add_command(
        #     label=PagesEnum.Page1.value,
        #     command=lambda: parent.show_frame(PagesEnum.Page1)
        # )
        # pages_menu.add_command(
        #     label=PagesEnum.Page2.value,
        #     command=lambda: parent.show_frame(PagesEnum.Page2)
        # )
        # pages_menu.add_command(
        #     label='MatPlot Demo 001',
        #     command=lambda: parent.show_frame(PagesEnum.matplotpage1)
        # )
        # pages_menu.add_command(
        #     label='Questionnaire',
        #     command=lambda: parent.show_frame(PagesEnum.Questionnaire)
        # )
        # pages_menu.add_command(
        #     label='CanvasPage',
        #     command=lambda: parent.show_frame(PagesEnum.CanvasPage)
        # )

        file_menu = Menu(menubar, tearoff=False)
        file_menu.add_command(
            label='Reset',
            command=lambda: parent.reset_app()
        )
        file_menu.add_command(
            label='Exit',
            command=lambda: parent.shutdown_app()
        )
        menubar.add_cascade(
            label="File",
            menu=file_menu,
            underline=0
        )

    @staticmethod
    def sayHello():
        print("Hello")