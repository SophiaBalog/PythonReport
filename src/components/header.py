import flet as ft
from src.styles import (
    HEADER_TITLE_STYLE
)

from src.styles import (
    REGISTER_BUTTON,
    LOGIN_BUTTON,
    NAV_BUTTON,
    HEADER_CONFIG,
    HEADER_ACTIONS_PADDING,

)

class Header(ft.AppBar):

    def __init__(self,
                 page: ft.Page,
                 page_name:str,
                 go_home = None,
                 go_courses=None,
                 go_profile=None,
                 go_login = None,
                 go_register = None,
                 ):
        self.page_name = page_name

        current_user = page.session.store.get("user")

        is_logged_in = bool(
            current_user and current_user.get("email")
        )

        if is_logged_in:
            buttons = [
                ft.Button("Home", on_click=go_home,style = NAV_BUTTON),
                ft.Button("Courses", on_click=go_courses,style = NAV_BUTTON),
                ft.Button("Profile", on_click=go_profile,style = NAV_BUTTON),
            ]
        else:
            buttons = [
                ft.Button("Login", on_click=go_login, style = LOGIN_BUTTON),
                ft.Button("Register", on_click=go_register, style = REGISTER_BUTTON),
            ]

        actions = [
            ft.Container(
                content=ft.Row(controls=buttons, spacing=10),
                padding=HEADER_ACTIONS_PADDING
            )
        ]

        super().__init__(
            title=ft.Text(page_name, style=HEADER_TITLE_STYLE),
            actions=actions,
            **HEADER_CONFIG
        )
