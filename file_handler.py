import json
import os
from datetime import datetime


FILENAME = "tasks.json"
VALID_STATUSES = ('todo', 'in-progress', 'done')


#Check if a file exists
def check_file_exists(filename):
    '''
    Check if a file exists. If it does not exist, create it.
    '''
    if not os.path.exists(filename):
        create_file(filename)
    

#Create, write and read a file
def create_file(filename):
    '''
    Create a JSON file if it does not exist. If the file already exists, do nothing.
    '''
    if not os.path.exists(filename):
        write_file(filename, [])

def write_file(filename, data):
    '''
    Write data to a JSON file.
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_file(filename):
    '''
    Read the contents of a JSON file and return it as a Python object.
    '''
    check_file_exists(filename)
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

    
#Add, update and delete tasks
def add_task(filename, description=None):
    '''
    Add a new task to JSON file.
    '''
    check_file_exists(filename)
    tasks = read_file(filename)

    new_id = max([task['id'] for task in tasks], default=0) + 1
    createdAt = datetime.now().isoformat()
    updatedAt = createdAt

    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': createdAt,
        'updatedAt': updatedAt
    }
    
    tasks.append(new_task)
    write_file(filename, tasks)

    return new_id
    
def update_task(filename, task_id, description=None, status=None):
    '''
    Update an existing task in the JSON file.
    '''
    check_file_exists(filename)
    tasks = read_file(filename)

    flag_found = False
    for task in tasks:
        if task['id'] == int(task_id):
            if description is not None:
                task['description'] = description
            if status is not None:
                task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            flag_found = True
            break

    if not(flag_found):
        return False
    
    write_file(filename, tasks)
    return True

def delete_task(filename, task_id):
    '''
    Delete a task from the JSON file.
    '''
    check_file_exists(filename)
    tasks = read_file(filename)

    flag_found = False
    for task in tasks:
        if task['id'] == int(task_id):
            tasks.remove(task)
            flag_found = True
            break

    if not(flag_found):
        return False
    
    write_file(filename, tasks)
    return True    


#Filter tasks by status
def list_tasks_by_status(filename, status):
    '''
    List tasks filtered by status.
    '''
    if status not in VALID_STATUSES:
        return False
    
    check_file_exists(filename)
    tasks = read_file(filename)

    filtered_tasks = [task for task in tasks if task['status'] == status]
    filtered_tasks = [format_task(task) for task in filtered_tasks]
    return filtered_tasks


#Output all tasks
def list_all_tasks(filename):
    '''
    List all tasks.
    '''
    check_file_exists(filename)
    tasks = read_file(filename)
    tasks = [format_task(task) for task in tasks]

    return tasks


#Format task for output
def format_task(task):
    '''
    Format a task for output.
    '''
    return f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}"