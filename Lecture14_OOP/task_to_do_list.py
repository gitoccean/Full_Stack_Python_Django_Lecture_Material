class Task:
    def _init_(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.status = "Not Done"
        self.due_date = due_date

    def mark_as_completed(self):
        self.status = "Done"

    def _str_(self):
        return f"Name: {self.name}, Priority: {self.priority}, Status: {self.status}, Due Date: {self.due_date}"

class TaskManager:
    def _init_(self):
        self.tasks = []

    def add_task(self, name, priority, due_date):
        task = Task(name, priority, due_date)
        self.tasks.append(task)
        print(f"Task '{name}' has been added.")

    def list_tasks(self):
        if not self.tasks:
            print("Task list is empty.")
        else:
            print("Current Tasks: ")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def mark_task_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_as_completed()
            print(f"Task '{self.tasks[task_number - 1].name}' has been marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_name):
        updated_tasks = []
        task_found = False
        for task in self.tasks:
            if task.name == task_name:
                print(f"Task '{task_name}' has been deleted.")
                task_found = True
            else:
                updated_tasks.append(task)
        if not task_found:
            print(f"'{task_name}' not found in the list.")
        self.tasks = updated_tasks

    def quit_task_manager(self):
        print("Thanks for using our task management app.")
        exit()

def main():
    task_manager = TaskManager()

    while True:
        print("Task Management Menu: ")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            priority = input("Enter task priority (High, Medium, Low): ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            task_manager.add_task(name, priority, due_date)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            task_manager.mark_task_complete(task_number)
        elif choice == '4':
            task_name = input("Enter task name to delete: ")
            task_manager.delete_task(task_name)
        elif choice == '5':
            task_manager.quit_task_manager()
        else:
            print("Invalid input. Please choose from the given options.")

if __name__ == "__main__":
    main()
