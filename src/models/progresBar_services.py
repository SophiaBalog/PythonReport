from .user_services import UsersService


class ProgresBarServices:
    def __init__(self,current_user):
        self.user = UsersService(current_user).get_user()

    def get_theme_progress(self, lessons):
        progress = self.user.get("progress", {})

        completed = 0
        total = len(lessons)

        for lesson in lessons:
            lesson_id = lesson["id"]

            if lesson_id in progress:
                lesson_result = progress[lesson_id]

                if lesson_result["score"] > 0:
                    completed += 1

        if total == 0:
            return 0
        return completed / total

    def get_subject_progress(self, subject):
        themes = subject.get("themes", [])

        if not themes:
            return 0

        total_percent = 0

        for theme in themes:
            theme_progress = self.get_theme_progress(theme["lessons"])
            total_percent += theme_progress

        result = total_percent / len(themes)
        return result
