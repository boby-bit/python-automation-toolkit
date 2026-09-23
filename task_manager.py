TASK_FILE = 'tasks.txt'

def add_task(task):
    with open(TASK_FILE, 'a') as f:
        f.write(task + '\n')

def view_tasks():
    print('\nTasks:')
    try:
        with open(TASK_FILE, 'r') as f:
            for i, task in enumerate(f, 1):
                print(f'{i}. {task.strip()}')
    except FileNotFoundError:
        print('No tasks found')
