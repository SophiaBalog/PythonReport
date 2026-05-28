import flet as ft
from src.models import RegisterUser

from src.styles import (
    GRADIENT,
    HEADER_H1,
    LOGIN_CARD_CONFIG,
    ERROR_TEXT_STYLE,
    INPUT_LOGIN_STYLE,
    REGISTER_BUTTON,
    NAV_BUTTON,
)

class RegisterView(ft.View):
    def __init__(self,page):

        async def go_login():
            await self.page.push_route('/login')

        async def go_login2():
            result = RegisterUser(username.value,user_email.value,password.value).check()
            if result['success']:
                result_text.value = ""
                await self.page.push_route('/login')
            else:
                result_text.value = result['message']

        super().__init__(
            route='/register',
            padding=0,
            controls=[
                ft.Container(
                    expand=True,
                    gradient=GRADIENT,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[

                            ft.Text("Learniva", style=HEADER_H1),
                            ft.Container(height=20),

                            ft.Container(
                                **LOGIN_CARD_CONFIG,
                                content=ft.Column([
                                    ft.Text("Реєстрація", size=24),
                                    username := ft.TextField(
                                        label="Нік користувача",
                                        **INPUT_LOGIN_STYLE,
                                        prefix_icon=ft.Icons.PERSON_OUTLINE,
                                    ),

                                    user_email := ft.TextField(
                                        label="Email",
                                        **INPUT_LOGIN_STYLE,
                                        prefix_icon=ft.Icons.EMAIL_OUTLINED,
                                        keyboard_type=ft.KeyboardType.EMAIL
                                    ),

                                    password := ft.TextField(
                                        label="Пароль",
                                        password=True,
                                        can_reveal_password=True,
                                        **INPUT_LOGIN_STYLE,
                                        prefix_icon=ft.Icons.LOCK_OUTLINE,
                                    ),

                                    result_text := ft.Text('', style=ERROR_TEXT_STYLE),

                                    ft.Button(
                                        'Зареєструватися',
                                        on_click=go_login2,
                                        style=REGISTER_BUTTON,
                                        width=400,
                                    ),

                                    ft.Row([
                                        ft.Text("Вже маєте акаунт?", size=14),
                                        ft.TextButton(
                                            'Увійти',
                                            on_click=go_login,
                                            style=NAV_BUTTON
                                        ),
                                    ], alignment=ft.MainAxisAlignment.CENTER),
                                ],
                                    spacing=15,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                ),
                            )
                        ]
                    )
                )
            ],
        )


