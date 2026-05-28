import flet as ft
from src.components import (
    Header,
    Footer
)

from src.models import (
    CourseService,
    ProgresBarServices
)

from src.styles import (
    HEADER_H1,
    TEXT_SECONDARY,
    THEME_CARD_STYLE,
    THEME_GRID_CONFIG,
    HEADER_H2,
    DARK,
    PROGRESS_BAR_COLOR,
    PROGRESS_BG_COLOR,
    LESSON_TILE_STYLE,
    LABEL_BOLD,
    PRIMARY_YELLOW
)

class CourseView(ft.View):
    def __init__(self,page,subject):
        self.subject = subject
        self.user = page.session.store.get('user')
        self.course = CourseService().get_course(self.subject)
        self.progress_service = ProgresBarServices(self.user)

        async def go_lessons(e):
            await self.page.push_route(f'/course/{subject}/{e.control.data}')

        async def go_home():
            await self.page.push_route('/home')

        async def go_courses():
            await self.page.push_route('/courses')

        async def go_profile():
            await self.page.push_route('/profile')


        self.header = Header(page,'Learniva',go_profile=go_profile,go_home = go_home,go_courses= go_courses)
        self.footer = Footer()

        super().__init__(
            route=f'/course/{subject}',
            scroll=ft.ScrollMode.AUTO,
            appbar=self.header,
            padding=0,
            controls=[
                ft.Container(
                    padding=ft.Padding(40, 40, 40, 20),
                    content=ft.Column([
                        ft.Text(f"Курс: {self.course['title']}", style=HEADER_H1),
                        ft.Text("Оберіть тему для вивчення", size=16, color=TEXT_SECONDARY),
                    ], spacing=5)
                ),

                ft.Container(
                    padding=ft.Padding(40, 0, 40, 40),
                    content=ft.GridView(
                        **THEME_GRID_CONFIG,
                        controls=[
                            ft.Container(
                                **THEME_CARD_STYLE,
                                content=ft.Column([
                                    ft.Text(i['title'], style=HEADER_H2),
                                    ft.Column([
                                        ft.Row([
                                            ft.Text("Прогрес теми", size=12, color=TEXT_SECONDARY),
                                            ft.Text(value=self.progress_service.get_theme_progress(i["lessons"])*100, size=12, color=DARK),
                                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                        ft.ProgressBar(
                                            width=None,
                                            value=self.progress_service.get_theme_progress(i['lessons']),
                                            color=PROGRESS_BAR_COLOR,
                                            bgcolor=PROGRESS_BG_COLOR,
                                            height=8
                                        ),
                                    ], spacing=5),


                                    ft.Divider(height=10, color="transparent"),

                                    ft.Column(
                                        scroll=ft.ScrollMode.AUTO,
                                        expand=True,
                                        spacing=10,
                                        controls=[
                                            ft.Container(
                                                **LESSON_TILE_STYLE,
                                                padding=ft.Padding(15, 5, 10, 5),
                                                content=ft.ListTile(
                                                    title=ft.Text(j['title'], style=LABEL_BOLD),
                                                    leading=ft.Container(
                                                        content=ft.Text(f'{n}', size=12),
                                                        bgcolor=PRIMARY_YELLOW,
                                                        width=30, height=30,
                                                        border_radius=15,
                                                        alignment=ft.Alignment.CENTER
                                                    ),
                                                    trailing=ft.IconButton(
                                                        ft.Icons.PLAY_CIRCLE_FILL,
                                                        icon_color=DARK,
                                                        on_click=go_lessons,
                                                        data=j['id']
                                                    ),
                                                )
                                            ) for n, j in enumerate(i['lessons'], 1)
                                        ]
                                    )
                                ], spacing=20)
                            ) for i in self.course['themes']
                        ]
                    )
                ),
                self.footer
            ],
        )