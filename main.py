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

if __name__ == "__main__":
    sample_task = Task(1, "Study ООP", 1)
    print("It works")
    print(sample_task)