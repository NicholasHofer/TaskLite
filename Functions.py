import json
import os
from datetime import datetime

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

def add_task(taskName):
    try:
        # Load existing tasks or start with an empty list
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                try:
                    tasks = json.load(file)
                except json.JSONDecodeError:
                    tasks = []
        else:
            tasks = []

        # Increment id by 1
        newID = tasks[-1]['id'] + 1 if tasks != [] else 1
        
        # Add task to tasks.json
        myTask = Task(newID, taskName, "todo", str(datetime.now()), str(datetime.now()))
        myTaskJSON = {"id":myTask.id, 
                    "description":myTask.description, 
                    "status":myTask.status, 
                    "createdAt":myTask.createdAt, 
                    "updatedAt":myTask.updatedAt}
    
        tasks.append(myTaskJSON)

        # Save task to file
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
        
        print(f'\033[92mTask "{taskName}" has been created with ID {newID}\033[0m')
        list_all()

    except Exception as e:
        print(f"An error occurred while adding the task: {e}")

def modify_task(id, description):
    if not os.path.exists('tasks.json'):
        print("Task file not found.")
        return

    with open('tasks.json', 'r') as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            print("Error reading tasks file.")
            return

    found = False
    for task in tasks:
        if str(task.get('id')) == str(id): 
            old_description = task.get('description', '')
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            found = True
            break

    if not found:
        print(f"Task with ID {id} not found.")
        return

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task ID {id} updated:\n  {old_description} --> {description}")     


def delete_task(id):
    # check if file/task exists
    if not os.path.exists('tasks.json'):
        print('Task not found')
        return
    
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except:
        print('Task not found')
        return

    # if task exists, delete it
    for t, task in enumerate(tasks):
        if task.get('id') == id:
            del tasks[t]
            # persist changes to file
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f, ensure_ascii=False, indent=4) 
            print(f"Task ID {id} has been deleted")   
            return
        
    # if task does not exist, print message
    print('Task not found')

def update_status(id, status):
    if not os.path.exists('tasks.json'):
        print("Task file not found.")
        return

    with open('tasks.json', 'r') as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            print("Error reading tasks file.")
            return

    found = False
    for task in tasks:
        if str(task.get('id')) == str(id): 
            old_status = task.get('status', '')
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            found = True
            break

    if not found:
        print(f"Task with ID {id} not found.")
        return

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task ID {id} updated:\n  {old_status} --> {status}")    


def list_all():
    # check if file/tasks exist
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            try:
                # print all tasks in file
                tasks = json.load(f)
                print(f"{'ID':<5} {'DESCRIPTION':<30} {'STATUS':<15} {'CREATED AT':<30} {'UPDATED AT':<30}")
                for task in tasks:
                    t = Task(task['id'], task['description'], task['status'], task['createdAt'], task['updatedAt'])
                    print(f"{t.id:<5} {t.description:<30} {t.status:<15} {t.createdAt:<30} {t.updatedAt:<30}")
            except:
                print('No tasks found')
    else:
        print('No tasks found')

def list_by_status(status):
    # check if any tasks exist with provided status
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            try:
                # print only tasks with task status = status param
                tasks = json.load(f)
                print(f"{'ID':<5} {'DESCRIPTION':<30} {'STATUS':<15} {'CREATED AT':<30} {'UPDATED AT':<30}")
                for task in tasks:
                    t = Task(task['id'], task['description'], task['status'], task['createdAt'], task['updatedAt'])
                    if t.status == status.lower():
                        print(f"{t.id:<5} {t.description:<30} {t.status:<15} {t.createdAt:<30} {t.updatedAt:<30}")
            except:
                print(f'No tasks found with status: {status}')
    else:
        print(f'No tasks found with status: {status}')