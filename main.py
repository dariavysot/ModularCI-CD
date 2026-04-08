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

    def load_tasks(self):
        tasks_list = []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 5:
                        t_id, desc, prio, date, done = parts
                        task = Task(int(t_id), desc, int(prio), date, done == 'True')
                        tasks_list.append(task)
        except FileNotFoundError:
            return []
        return tasks_list

    def list_tasks_sorted(self, sort_by="priority"):
        tasks = self.load_tasks()
        if sort_by == "priority":
            tasks.sort(key=lambda x: x.priority)
        elif sort_by == "date":
            tasks.sort(key=lambda x: x.created_at)
        
        return tasks

    def save_to_file(self, task):
        with open(self.filename, "a", encoding="utf-8") as f:
            line = f"{task.task_id}|{task.description}|{task.priority}|{task.created_at}|{task.is_done}\n"
            f.write(line)
        print(f"Task '{task.description}' saved to tasks.txt")

if __name__ == "__main__":
    manager = TaskManager()

    print("---tasks from the file ---")
    current_tasks = manager.load_tasks()
    for t in current_tasks:
        print(t)

    print("--- Creating task ---")
    desc = input("What needs to be done? ")
    prio = input("What is the priority (1-5)? ")

    new_id = len(current_tasks) + 1
    new_task = Task(new_id, desc, prio)
    manager.save_to_file(new_task)
