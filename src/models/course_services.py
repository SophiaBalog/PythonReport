from .load_json import JsonService

class CourseService:
    def __init__(self):
        self.json_service = JsonService('storage/courses.json')
        self.courses = self.json_service.read_json()

    def get_course(self,subject):
        for i in self.courses:
            if i.get("data") == subject:
                return i
        return None

    def get_lesson(self, lesson_id: str):
        """Знайти конкретний урок по id"""
        for course in self.courses:
            for theme in course.get("themes", []):
                for lesson in theme.get("lessons", []):
                    if lesson.get("id") == lesson_id:
                        return lesson
        return None