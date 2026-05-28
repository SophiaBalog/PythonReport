import flet as ft

from src.views import (
    LandingView,
    LoginView,
    RegisterView,
    HomeView,
    CoursesView,
    CourseView,
    LessonView,
    ProfileView,
)
from src.views.test import TestView


class App:
    def __init__(self, page: ft.Page):
        self.page = page

        self.page.on_view_pop = self.view_pop
        self.page.on_route_change = self.route_change
        self.route_change(None)

    def route_change(self, route):
        self.page.views.clear()

        current_user = self.page.session.store.get("user")

        is_logged_in = bool(
            current_user and current_user.get("email")
        )

        if is_logged_in:
            self.page.views.append(HomeView(self.page))
        else:
            self.page.views.append(LandingView(self.page))

        route_parts = self.page.route.strip("/").split("/")

        if self.page.route == "/login":
            self.page.views.append(
                LoginView(self.page)
            )
        elif self.page.route == "/register":
            self.page.views.append(
                RegisterView(self.page)
            )
        elif self.page.route == "/home":
            self.page.views.append(
                HomeView(self.page)
            )
        elif self.page.route == "/home/profile":
            self.page.views.append(
                ProfileView(self.page)
            )
        elif self.page.route == "/home/courses":
            self.page.views.append(
                CoursesView(self.page)
            )
        elif len(route_parts) == 2 and route_parts[0] == "course":
            course_key = route_parts[1]
            self.page.views.append(
                CourseView(
                    self.page,
                    course_key
                )
            )
        elif len(route_parts) == 3 and route_parts[0] == "course":

            course_key = route_parts[1]
            lesson_id = route_parts[2]
            self.page.views.append(
                LessonView(
                    self.page,
                    course_key,
                    lesson_id
                )
            )

        elif len(route_parts) == 4 and route_parts[0] == "course":

            course_key = route_parts[1]
            lesson_id = route_parts[2]
            theme = route_parts[3]
            self.page.views.append(
                TestView(
                    self.page,
                    course_key,
                    lesson_id,
                    theme
                )
            )

        self.page.update()

    async def view_pop(self, e):
        if len(self.page.views) > 1:
            self.page.views.pop()
            await self.page.push_route(self.page.views[-1].route)


def main(page: ft.Page):
    App(page)


if __name__ == '__main__':
    ft.run(main, view=ft.AppView.WEB_BROWSER)
import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


ft.run(main)
