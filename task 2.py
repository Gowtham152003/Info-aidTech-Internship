import pickle

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "Not Done"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print(f"Task '{title}' added to the to-do list.")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted from the to-do list.")
                break
        else:
            print(f"Task '{title}' not found in the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks in the to-do list:")
            for task in self.tasks:
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Status: {task.status}")
                print("-" * 30)

    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)
        print(f"Tasks saved to '{filename}'.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
            print(f"Tasks loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"'{filename}' not found. No tasks loaded.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            to_do_list.add_task(title, description)
        elif choice == "2":
            title = input("Enter the title of the task to delete: ")
            to_do_list.delete_task(title)
        elif choice == "3":
            to_do_list.view_tasks()
        elif choice == "4":
            filename = input("Enter the filename to save tasks: ")
            to_do_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter the filename to load tasks: ")
            to_do_list.load_tasks(filename)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
