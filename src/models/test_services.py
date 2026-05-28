from .load_json import JsonService


class TestService:
    def __init__(self):
        self.db = JsonService("storage/users.json")

    def check_answers(self, questions, selected_answers):
        score = 0
        mistakes = []

        for i, q in enumerate(questions):
            correct = q["correct"]
            user = selected_answers.get(i)

            if user == correct:
                score += 1
            else:
                mistakes.append({
                    "index": i + 1,
                    "question": q["question"],
                    "user": user,
                    "correct": correct,
                    "answers": q["answers"]
                })

        return score, mistakes

    def save_progress(self, user, lesson_id, score, total):
        users = self.db.read_json()

        for u in users:
            if u["email"] == user["email"]:

                if "progress" not in u:
                    u["progress"] = {}

                u["progress"][lesson_id] = {
                    "score": score,
                    "total": total
                }

                break

        self.db.dump_json(users)