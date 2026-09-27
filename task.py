class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✅" if self.done else "❌"
        return f"{status} {self.title} (до {self.deadline})"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_all(self):
        for task in self.tasks:
            print(task)
manager = TaskManager()
manager.add_task(Task("Сдать лабу", "2026-09-25"))
manager.add_task(Task("Сходить в спортзал", "2026-09-26"))
manager.show_all()

t = Task("Сдать лабу", "2026-09-25")
print(t.title, t.done)
t.mark_done()
print(t.done)
print(t)
