import flet as ft
from src.components import (
    Header,
    Footer
)

from src.models import (
    JsonService,
)

from src.styles import (
    COURSE_TITLE_STYLE,
    COURSE_CARD_STYLE,
    COURSE_GRID_CONFIG,
    HEADER_H1,
    COURSE_BUTTON_STYLE,
    TEXT_SECONDARY,
)

class CoursesView(ft.View):
    def __init__(self,page):
        async def go_home():
            await self.page.push_route('/home/courses')

        async def go_profile():
            await self.page.push_route('/home/profile')

        async def go_course(e):
            course_key = e.control.data
            await self.page.push_route(f"/course/{course_key}")

        self.header = Header(page,'Learniva',go_home = go_home,go_profile= go_profile)
        self.footer = Footer()
        self.cards = JsonService('storage/courses.json').read_json()

        super().__init__(
            route='/home/courses',
            scroll=ft.ScrollMode.AUTO,
            appbar=self.header,
            padding=0,
            controls=[
                ft.Container(
                    padding=ft.Padding(40, 40, 40, 20),
                    content=ft.Text("Доступні курси", style=HEADER_H1)
                ),

                ft.Container(
                    padding=ft.Padding(40, 20, 40, 20),
                    content=ft.GridView(
                        **COURSE_GRID_CONFIG,
                        controls=[
                            ft.Container(
                                **COURSE_CARD_STYLE,
                                content=ft.Column([
                                    ft.Image(
                                        src=card['image'],
                                        width=400,
                                        height=200,
                                        border_radius=ft.BorderRadius.only(top_left=15, top_right=15)
                                    ),
                                    ft.Container(
                                        padding=ft.Padding(20, 15, 20, 20),
                                        content=ft.Column([
                                            ft.Text(card['title'], style=COURSE_TITLE_STYLE),
                                            ft.Text(
                                                card['description'],
                                                size=14,
                                                color=TEXT_SECONDARY,
                                                max_lines=3,
                                                overflow=ft.TextOverflow.ELLIPSIS
                                            ),
                                            ft.Container(expand=True),
                                            ft.Button(
                                                'Перейти до курсу',
                                                data=card["data"],
                                                on_click=go_course,
                                                style=COURSE_BUTTON_STYLE,
                                                width=400
                                            )
                                        ], spacing=10, expand=True)
                                    )
                                ], spacing=0)
                            ) for card in self.cards
                        ]
                    )
                ),
                self.footer
            ]
        )