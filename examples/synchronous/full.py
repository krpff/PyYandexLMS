from os import getenv

from PyYandexLMS.errors import ApiError
from PyYandexLMS.synchronous import Client

login = getenv("LOGIN")
password = getenv("PASSWORD")


def main():
    client = Client(login, password)
    user = client.get_user()
    print(f"Имя: {user.profile.display_name}")
    print(f"Дата регистрации в LMS: {user.profile.date_joined.strftime('%d.%m.%Y')}")
    for course in user.courses_summary.student:
        print(f"---- Курс: {course.title} ----")
        try:
            lessons = client.get_lessons(course)
            for lesson in lessons:
                print(f"Урок: {lesson.title}")
                materials = client.get_materials(lesson)
                print(f"Количество материалов: {len(materials)}")
                tasks = client.get_tasks(lesson.id, course.id, course.group.id)
                print(f"Количество заданий: {len(tasks)}")
                for task_type in tasks:
                    if task_type.tasks:
                        for task in task_type.tasks:
                            print(task.title)
                            if task.solution.status != "new":
                                solution = client.get_solution(solution_id=task.solution.id)
                                print(f"Решение: #{solution.solution.id}")
        except ApiError as e:
            print(f"Ошибка: {e.message}")


if __name__ == "__main__":
    main()
