import flet as ft
from src.components import (
    Header,
    Footer
)
from src.models import (
    UsersService,
    JsonService,
    ProgresBarServices
)

from src.styles import (
    BORDER,
    CARD_BG,
    HEADER_H2,
    LABEL_BOLD,
    BODY_MEDIUM,
    BODY_SMALL,
    BASE_BUTTON,
    BORDER_LIGHT,
    PRIMARY_YELLOW,
    TEXT_SECONDARY,
    PRIMARY_YELLOW_DARK,
    PRIMARY_YELLOW_LIGHT,

)


class ProfileView(ft.View):
    def __init__(self,page):
        self.current_user = page.session.store.get("user")
        self.user = UsersService(self.current_user).get_user()
        self.progress_service = ProgresBarServices(self.current_user)

        async def go_home():
            await self.page.push_route('/home')

        async def go_courses():
            await self.page.push_route('/home/courses')

        def update_avatar(e):
            new_avatar = UsersService(self.user['name']).update_avatar()['avatar']
            avatar.src = new_avatar
            page.update()

        self.header = Header(page,'Learniva',go_home = go_home,go_courses= go_courses)
        self.footer = Footer()
        self.courses = JsonService('storage/courses.json').read_json()


        super().__init__(
            route=f'/home/profile',
            scroll=ft.ScrollMode.AUTO,
            appbar=self.header,
            controls = [

                ft.Container(
                    padding=40,
                    bgcolor=CARD_BG,
                    border_radius=20,
                    border=ft.border.all(1, BORDER),
                    content=ft.Row([
                        ft.Column([
                            ft.Container(
                                width=150,
                                height=150,
                                border_radius=75,
                                content = ( avatar:= ft.Image(src = self.user['avatar']))
                            ),
                            ft.Button(
                                'Змінити фото',
                                on_click=update_avatar,
                                style=BASE_BUTTON,
                                icon=ft.Icons.EDIT_OUTLINED,
                                icon_color=TEXT_SECONDARY
                            )
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
                        ft.Column([
                            ft.Row([
                                ft.Text(f"{self.user['name']}".capitalize(), style=HEADER_H2),
                                ft.Container(
                                    content=ft.Text("ЗНО-2025", size=12, color=PRIMARY_YELLOW_DARK),
                                    bgcolor=PRIMARY_YELLOW_LIGHT,
                                    border_radius=15
                                )
                            ], alignment=ft.MainAxisAlignment.START),

                            ft.Text(f"{self.user.get('email')}", style=BODY_MEDIUM),

                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            ft.ListTile(
                                content_padding=0,
                                leading=ft.Icon(ft.Icons.CALENDAR_MONTH, color=TEXT_SECONDARY),
                                title=ft.Text('Дата реєстрації', style=BODY_SMALL),
                                subtitle=ft.Text(
                                    f"{self.user['data']}",
                                    style=LABEL_BOLD
                                )
                            )

                        ], expand=True, spacing=10, alignment=ft.MainAxisAlignment.CENTER)

                    ], spacing=40, vertical_alignment=ft.CrossAxisAlignment.START)
                ),


                ft.Container(
                    padding=ft.padding.only(top=20),
                    content=ft.Column([
                        ft.Container(
                            bgcolor=CARD_BG,
                            border_radius=12,
                            padding=10,
                            border=ft.Border.all(1, BORDER_LIGHT),
                            content=ft.Row([
                                ft.Container(
                                    expand=True,
                                    content=ft.ListTile(
                                        title=ft.Text(i['title'], style=LABEL_BOLD),
                                    )
                                ),
                                ft.Column([
                                    ft.Text(f"Прогрес {round(self.progress_service.get_subject_progress(i) * 100)}%", style=BODY_SMALL),
                                    ft.ProgressBar(
                                        value=self.progress_service.get_subject_progress(i),
                                        width=250,
                                        color=PRIMARY_YELLOW,
                                        bgcolor=BORDER_LIGHT
                                    )
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5)
                            ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
                        ) for i in self.courses
                    ], spacing=10)
                ),
                self.footer
            ]

        )



