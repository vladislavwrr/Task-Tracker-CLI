import sys
import file_handler as fh

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: python task_cli.py <command> [arguments]")
        return

    command = args[0]

    if command == "add":
        if len(args) < 2 or not args[1].strip():
            print("Usage: task_cli.py add <description>")
            return
        description = " ".join(args[1:]).strip()
        task_id = fh.add_task(fh.FILENAME, description)
        print(f"Task added successfully (ID: {task_id})")

    elif command == "update":
        if len(args) != 3 or not args[2].strip():
            print("Usage: task_cli.py update <task_id> <description>")
            return
        if not(args[1].isdigit()):
            print("Error: task_id must be an integer.")
            return
        task_id = args[1]
        description = args[2].strip()

        success = fh.update_task(fh.FILENAME, task_id, description, None)
        if success:
            print(f"Task {task_id} updated.")
        else:
            print(f"Task {task_id} not found.")

    elif command == "delete":
        if len(args) != 2:
            print("Usage: task_cli.py delete <task_id>")
            return
        if not(args[1].isdigit()):
            print("Error: task_id must be an integer.")
            return
        task_id = args[1]
        success = fh.delete_task(fh.FILENAME, task_id)
        if success:
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task {task_id} not found.")

    elif command == "list":
        if len(args) == 1:
            tasks = fh.list_all_tasks(fh.FILENAME)
            if not(tasks):
                print("No tasks found.")
                return
            for task in tasks:
                print(task)
        elif len(args) == 2:
            status = args[1]
            tasks = fh.list_tasks_by_status(fh.FILENAME, status)
            if tasks is False:
                print(f"Error: Invalid status '{status}'. Available: todo, in-progress, done")
                return
            elif not(tasks):
                print(f"No tasks found with status '{status}'.")  
                return  
            for task in tasks:
                print(task)
        else:
            print("Usage: task_cli.py list [status]")
            return

    elif command == "mark-todo":
        if len(args) != 2:
            print("Usage: task_cli.py mark-todo <task_id>")
            return
        if not(args[1].isdigit()):
            print("Error: task_id must be an integer.")
            return
        task_id = args[1]
        success = fh.update_task(fh.FILENAME, task_id, status='todo')
        if success:
            print(f"Task {task_id} marked as todo.")
        else:
            print(f"Task {task_id} not found.")                        

    elif command == "mark-in-progress":
        if len(args) != 2:
            print("Usage: task_cli.py mark-in-progress <task_id>")
            return
        if not(args[1].isdigit()):
            print("Error: task_id must be an integer.")
            return
        task_id = args[1]
        success = fh.update_task(fh.FILENAME, task_id, status='in-progress')
        if success:
            print(f"Task {task_id} marked as in-progress.")
        else:
            print(f"Task {task_id} not found.")

    elif command == "mark-done":
        if len(args) != 2:
            print("Usage: task_cli.py mark-done <task_id>")
            return
        if not(args[1].isdigit()):
            print("Error: task_id must be an integer.")
            return
        task_id = args[1]
        success = fh.update_task(fh.FILENAME, task_id, status='done')
        if success:
            print(f"Task {task_id} marked as done.")
        else:
            print(f"Task {task_id} not found.")
        
    else:
        print(f"Unknown command: {command}")
        

if __name__ == "__main__":
    main()