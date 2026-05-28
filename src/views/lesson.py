import flet as ft
from src.components import (
    Header,
    Footer
)

from src.models import (
    CourseService
)

from src.styles import (
    HEADER_H1,
    TEXT_SECONDARY,
    VIDEO_TEXT_STYLE,
    VIDEO_SUBTITLE_STYLE,
    VIDEO_CARD_STYLE,
    PRIMARY_YELLOW,
    LESSON_CONTENT_STYLE,
    TESTING_BUTTON
)

class  LessonView(ft.View):
    def __init__(self,page,subject,lesson):
        self.subject = subject
        self.course = CourseService().get_course(self.subject)
        self.lesson = CourseService().get_lesson(lesson)

        async def open_video():
            await page.launch_url(self.lesson["video"])

        async def go_test(e):
            await page.push_route(f'/course/{subject}/{lesson}/{e.control.data}')

        async def go_profile():
            await self.page.push_route('/profile')

        async def go_home():
            await self.page.push_route('/home')

        async def go_courses():
            await self.page.push_route('/courses')


        self.header = Header(page,'Learniva',go_profile=go_profile,go_home = go_home,go_courses= go_courses)
        self.footer = Footer()

        super().__init__(
            route=f'/course/{subject}/{lesson}',
            scroll=ft.ScrollMode.AUTO,
            appbar=self.header,
            padding=0,
            controls=[
                ft.Container(
                    padding=ft.Padding(40, 40, 40, 60),
                    content=ft.Column([
                        ft.TextButton(
                            "← Повернутися до тем",
                            on_click=lambda _: page.go(f'/course/{subject}'),
                            style=ft.ButtonStyle(color=TEXT_SECONDARY)
                        ),

                        ft.Text(self.lesson['title'], style=HEADER_H1),
                        ft.Divider(height=20, color="transparent"),

                        ft.Container(
                            **VIDEO_CARD_STYLE,
                            on_click=open_video,
                            content=ft.ListTile(
                                leading=ft.Icon(ft.Icons.PLAY_CIRCLE_FILL, color=PRIMARY_YELLOW, size=40),
                                title=ft.Text("Відео-лекція до уроку", style=VIDEO_TEXT_STYLE),
                                subtitle=ft.Text("Натисніть, щоб відкрити плеєр YouTube", style=VIDEO_SUBTITLE_STYLE),
                                trailing=ft.Icon(ft.Icons.OPEN_IN_NEW, color="#9CA3AF", size=20),
                            )
                        ),

                        ft.Divider(height=30, color="transparent"),

                        ft.Text("Конспект уроку", style=HEADER_H1, size=24),
                        ft.Container(
                            **LESSON_CONTENT_STYLE,
                            content=ft.Column([
                                ft.Markdown(f"Додаткові матеріали: {self.lesson['content']}",
                                            )
                            ], spacing=15,
                            expand=True),
                            expand=True,
                            width=float("inf")
                        ),

                        ft.Divider(height=40, color="transparent"),


                        ft.Button(
                            "Перейти до тестування",
                            icon=ft.Icons.QUIZ,
                            on_click=go_test,
                            data = self.lesson['id'],
                            style= TESTING_BUTTON,
                            width=300
                        )
                    ], spacing=10)
                ),
                self.footer
            ],
        )