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
    
    def to_line(self):
        return f"{self.task_id}|{self.description}|{self.priority}|{self.created_at}|{self.is_done}\n"

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

    def _rewrite_file(self, tasks):
        with open(self.filename, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task.to_line())

    def remove_task(self, task_id):
        tasks = self.load_tasks()
        updated_tasks = [t for t in tasks if t.task_id != task_id]
        
        if len(tasks) == len(updated_tasks):
            print(f"Error: Task with ID {task_id} not found.")
        else:
            self._rewrite_file(updated_tasks)
            print(f"Task #{task_id} successufy deleted.")

    def complete_task(self, task_id):
        tasks = self.load_tasks()
        found = False
        for t in tasks:
            if t.task_id == task_id:
                t.is_done = True
                found = True
                break
        
        if found:
            updated_tasks = [t for t in tasks if not t.is_done]
            self._rewrite_file(updated_tasks)
            print(f"Task #{task_id} done and deleted.")
        else:
            print(f"Task #{task_id} not found.")

    def save_to_file(self, task):
        with open(self.filename, "a", encoding="utf-8") as f:
            line = f"{task.task_id}|{task.description}|{task.priority}|{task.created_at}|{task.is_done}\n"
            f.write(line)
        print(f"Task '{task.description}' saved to tasks.txt")

if __name__ == "__main__":
    manager = TaskManager()
    
    while True:
        print("\n=== TASK MANAGEMENT SYSTEM ===")
        print("1. View tasks (Sorted by Priority)")
        print("2. View tasks (Sorted by Date)")
        print("3. Add new task")
        print("4. Remove task by ID")
        print("5. Mark task as done (and remove)")
        print("0. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            print("\n--- Tasks by Priority ---")
            tasks = manager.list_tasks_sorted("priority")
            for t in tasks: print(t)
            
        elif choice == "2":
            print("\n--- Tasks by Date ---")
            tasks = manager.list_tasks_sorted("date")
            for t in tasks: print(t)
            
        elif choice == "3":
            print("\n--- Creating task ---")
            desc = input("Description: ")
            prio = input("Priority (1-5): ")
            current_tasks = manager.load_tasks()
            new_id = max([t.task_id for t in current_tasks], default=0) + 1
            manager.save_to_file(Task(new_id, desc, prio))
            
        elif choice == "4":
            try:
                t_id = int(input("Enter Task ID to remove: "))
                manager.remove_task(t_id)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == "5":
            try:
                t_id = int(input("Enter Task ID to mark as done: "))
                manager.complete_task(t_id)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Unknown option. Try again.")