import datetime

class Task:
    def __init__(self, task_id, description, priority, created_at=None, is_done=False):
        self.task_id = task_id
        self.description = description
        self.priority = int(priority)
        self.created_at = created_at if created_at else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_done = is_done

    def __str__(self):
        status = "done" if self.is_done else "in progres"
        return f"[{self.task_id}] {status} Priority: {self.priority} | {self.description} (Created: {self.created_at})"

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def save_to_file(self, task):
        with open(self.filename, "a", encoding="utf-8") as f:
            line = f"{task.task_id}|{task.description}|{task.priority}|{task.created_at}|{task.is_done}\n"
            f.write(line)
        print(f"Task '{task.description}' saved to tasks.txt")

if __name__ == "__main__":
    manager = TaskManager()
    new_task = Task(1, "Study ООP", 3)
    manager.save_to_file(new_task)