import flet as ft
from src.models import CourseService, TestService

from src.styles import (
    PRIMARY_YELLOW, BACKGROUND, CARD_BG,
    HEADER_H2, BODY_MEDIUM, LABEL_BOLD, BODY_LARGE,
    LOGIN_BUTTON
)


class TestView(ft.View):
    def __init__(self, page, subject, lesson, theme):
        self.subject = subject
        self.current_user = page.session.store.get('user')

        self.course = CourseService().get_course(self.subject)
        self.lesson = CourseService().get_lesson(lesson)

        self.questions = self.lesson["test"]["questions"]
        self.selected_answers = {}

        # --- Логіка ---
        async def go_home():
            await self.page.push_route('/home')

        async def close_alert(e):
            self.page.pop_dialog()
            await go_home()

        def save_answer(index, value):
            self.selected_answers[index] = value

        # --- Стилізований діалог результатів ---
        self.result_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Результат тесту", style=HEADER_H2),
            bgcolor=CARD_BG,
            shape=ft.RoundedRectangleBorder(radius=20),
            actions=[
                ft.TextButton("Зрозуміло", on_click=close_alert, style=LABEL_BOLD)
            ],
        )

        def check_test(e):
            service = TestService()
            score, mistakes = service.check_answers(self.questions, self.selected_answers)

            service.save_progress(
                user=self.current_user,
                lesson_id=self.lesson["id"],
                score=score,
                total=len(self.questions)
            )


            result_controls = [
                ft.Text(f"📊 Мій результат: {score}/{len(self.questions)}", style=HEADER_H2),
                ft.Divider(color=ft.Colors.TRANSPARENT, height=10)
            ]

            if mistakes:
                mistakes_list = ft.Column(scroll=ft.ScrollMode.AUTO, height=300, spacing=15)
                for m in mistakes:
                    user_ans = m["answers"][m["user"]] if m["user"] is not None else "не обрано"
                    correct_ans = m["answers"][m["correct"]]

                    mistakes_list.controls.append(
                        ft.Column([
                            ft.Text(f"{m['index']}. {m['question']}", style=LABEL_BOLD),
                            ft.Row([
                                ft.Icon(ft.Icons.CLOSE, color=ft.Colors.RED_400, size=16),
                                ft.Text(f"Твоя: {user_ans}", color=ft.Colors.RED_400, style=BODY_MEDIUM),
                            ], spacing=5),
                            ft.Row([
                                ft.Icon(ft.Icons.CHECK, color=ft.Colors.GREEN_400, size=16),
                                ft.Text(f"Правильна: {correct_ans}", color=ft.Colors.GREEN_400, style=BODY_MEDIUM),
                            ], spacing=5),
                        ], spacing=2)
                    )
                result_controls.append(mistakes_list)
            else:
                result_controls.append(ft.Text("🎉 Ідеально! Ти знаєш тему на всі 100%!", style=BODY_LARGE))

            self.result_dialog.content = ft.Column(result_controls, tight=True, width=400)
            self.page.show_dialog(self.result_dialog)
            self.page.update()

        # --- Основний інтерфейс ---
        super().__init__(
            route=f"/course/{subject}/{lesson}/{theme}",
            bgcolor=BACKGROUND,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        width=800,
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(bottom=20),
                                content=ft.Text(self.lesson["title"], style=HEADER_H2)
                            ),
                            *[
                                ft.Container(
                                    bgcolor=CARD_BG,
                                    padding=25,
                                    border_radius=20,
                                    margin=ft.margin.only(bottom=15),
                                    shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.with_opacity(0.05, "black")),
                                    content=ft.Column([
                                        ft.Text(f"Питання {n}", color=PRIMARY_YELLOW, style=LABEL_BOLD),
                                        ft.Text(i['question'], style=BODY_LARGE),
                                        ft.RadioGroup(
                                            content=ft.Column([
                                                ft.Radio(
                                                    label=j,
                                                    value=str(idx),
                                                    active_color=PRIMARY_YELLOW,
                                                    label_style=BODY_MEDIUM
                                                )
                                                for idx, j in enumerate(i['answers'])
                                            ], spacing=10),
                                            on_change=lambda e, q_idx=n - 1: save_answer(q_idx, int(e.control.value))
                                        )
                                    ], spacing=10)
                                )
                                for n, i in enumerate(self.questions, 1)
                            ],

                            ft.Container(
                                padding=ft.padding.only(top=20, bottom=40),
                                content=ft.ElevatedButton(
                                    "Перевірити результат",
                                    style=LOGIN_BUTTON,
                                    width=300,
                                    height=50,
                                    on_click=check_test
                                )
                            )
                        ]
                    )
                )
            ]
        )