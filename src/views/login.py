import flet as ft
from src.models import LoginUser
from src.styles import (
    GRADIENT,
    HEADER_H1,
    LOGIN_CARD_CONFIG,
    INPUT_LOGIN_STYLE,
    ERROR_TEXT_STYLE,
    LOGIN_BUTTON,
    NAV_BUTTON,
)


class LoginView(ft.View):
    def __init__(self,page):

        async def go_register():
            await self.page.push_route('/register')

        async def go_home():
            result = LoginUser(username.value,password.value).check(page)
            if result:
                await self.page.push_route('/home')
            else:
                result_text.value = 'Неправильне ім`я користувача або пароль'

        super().__init__(
            route='/login',
            padding=0,
            controls=[
                ft.Container(
                    expand=True,
                    gradient=GRADIENT,  # Використовуємо твій Hero-градієнт для фону
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Learniva", style=HEADER_H1),
                            ft.Container(height=20),

                            # Картка логінації
                            ft.Container(
                                **LOGIN_CARD_CONFIG,
                                content=ft.Column([
                                    ft.Text("Вхід у систему", size=24,),
                                    ft.Container(height=10),

                                    username := ft.TextField(
                                        label="Нік або Email",
                                        **INPUT_LOGIN_STYLE,
                                        prefix_icon=ft.Icons.PERSON_OUTLINE,
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
                                        'Увійти',
                                        on_click=go_home,
                                        style=LOGIN_BUTTON,
                                        width=400,  # Кнопка на всю ширину картки
                                    ),

                                    ft.Row([
                                        ft.Text("Ще не маєте акаунту?", size=14),
                                        ft.TextButton(
                                            'Створити акаунт',
                                            on_click=go_register,
                                            style=NAV_BUTTON  # Твій стиль для посилань
                                        ),
                                    ], alignment=ft.MainAxisAlignment.CENTER),
                                ], spacing=15),
                            )
                        ]
                    )
                )
            ],
        )

