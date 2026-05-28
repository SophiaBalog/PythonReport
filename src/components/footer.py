import flet as ft

from src.styles import FOOTER_CONFIG, FOOTER_TEXT_STYLE, FOOTER_LINK_STYLE


class Footer(ft.Container):
    def __init__(self):
        super().__init__(**FOOTER_CONFIG)

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        ft.Text("Курси", style=FOOTER_LINK_STYLE),
                        ft.Text("•", color="#4B5563"),
                        ft.Text("Тести", style=FOOTER_LINK_STYLE),
                        ft.Text("•", color="#4B5563"),
                        ft.Text("Прогрес", style=FOOTER_LINK_STYLE),
                        ft.Text("•", color="#4B5563"),
                        ft.Text("Практика", style=FOOTER_LINK_STYLE),
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "© 2026 ZNOHub — платформа для підготовки до НМТ. Усі права захищені.",
                            style=FOOTER_TEXT_STYLE
                        )
                    ]
                )
            ]
        )