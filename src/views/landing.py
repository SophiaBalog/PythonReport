import flet as ft

from src.components import (
    Header,
    Footer
)

from src.styles import (
    EASY_START_BUTTON,
    GRADIENT,
    HEADER_DISPLAY,
    BODY_LARGE,
    INFO_CARD_CONFIG,
    CARD_ICON_COLOR,
    CARD_ICON_SIZE,
    HEADER_H2,
    LABEL_BOLD,
    STAT_NUMBER_STYLE,
    BODY_SMALL,

)

from src.models import (
    JsonService,
)
class LandingView(ft.View):
    def __init__(self, page):
        self.current_user = JsonService('storage/session.json').read_json()

        self.hero_height = page.window.height - 300  if page.window.height else 630

        async def go_login(e):
            await self.page.push_route('/login')

        async def go_register(e):
            await self.page.push_route('/register')

        self.header = Header(page, 'Learniva', go_login=go_login, go_register=go_register)
        self.footer = Footer()

        super().__init__(
            route='/landing',
            scroll=ft.ScrollMode.AUTO,
            appbar=self.header,
            padding=0,
            spacing=0,
            controls=[

                ft.Container(
                    gradient=GRADIENT,
                    height=self.hero_height,
                    alignment=ft.Alignment.CENTER,
                    padding=ft.Padding.all(40),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                'Готуйся до НМТ/ЗНО без стресу',
                                style=HEADER_DISPLAY,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Container(
                                content=ft.Text(
                                    'Отримай доступ до актуальної бази тестів 2026 року, персональної аналітики знань та структурованих конспектів, розроблених спеціально для швидкого та ефективного навчання.',
                                    style=BODY_LARGE,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                width=800,
                                margin=ft.Margin.only(top=10, bottom=20)
                            ),
                            ft.Button(
                                'Швидкий старт',
                                on_click=go_login,
                                style=EASY_START_BUTTON
                            )
                        ],
                    )
                ),

                ft.Container(
                    padding=ft.Padding(40, 60, 40, 60),
                    bgcolor=ft.Colors.WHITE,
                    expand=True,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        spacing= 57,
                        wrap=True,
                        controls=[
                            # Картка 1: Чому ми?
                            ft.Container(
                                **INFO_CARD_CONFIG,
                                content=ft.Column([
                                    ft.Text('Чому ми?', style=HEADER_H2),
                                    ft.Row([ft.Icon(ft.Icons.TIMER, color=CARD_ICON_COLOR, size=CARD_ICON_SIZE),
                                            ft.Text('Навчання без графіків', style=LABEL_BOLD)]),
                                    ft.Row([ft.Icon(ft.Icons.REFRESH, color=CARD_ICON_COLOR, size=CARD_ICON_SIZE),
                                            ft.Text('Необмежена кількість спроб', style=LABEL_BOLD)]),
                                    ft.Row([ft.Icon(ft.Icons.BOLT, color=CARD_ICON_COLOR, size=CARD_ICON_SIZE),
                                            ft.Text('Миттєвий фідбек', style=LABEL_BOLD)]),
                                ], spacing=15),
                            ),

                            # Картка 2: Статистика
                            ft.Container(
                                **INFO_CARD_CONFIG,
                                content=ft.Column([
                                    ft.Text('Середній бал учнів', style=HEADER_H2),
                                    ft.Text('183/200', style=STAT_NUMBER_STYLE),
                                    ft.Text("Підготували понад 2000 учнів", style=BODY_SMALL)
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                            ),

                            # Картка 3: Платформа
                            ft.Container(
                                **INFO_CARD_CONFIG,
                                content=ft.Column([
                                    ft.Text('Що є на платформі', style=HEADER_H2),
                                    ft.Row([ft.Icon(ft.Icons.VIDEO_FILE, color=CARD_ICON_COLOR, size=CARD_ICON_SIZE),
                                            ft.Text('Відео уроки', style=LABEL_BOLD)]),
                                    ft.Row([ft.Icon(ft.Icons.TEXT_FORMAT, color=CARD_ICON_COLOR, size=CARD_ICON_SIZE),
                                            ft.Text('Пробники НМТ', style=LABEL_BOLD)]),
                                    ft.Row([ft.Icon(ft.Icons.BOOK, color=CARD_ICON_COLOR, size=CARD_ICON_SIZE),
                                            ft.Text('Структуровані конспекти', style=LABEL_BOLD)]),
                                ], spacing=15),
                            ),
                        ]
                    )
                ),
                self.footer
            ],
        )
