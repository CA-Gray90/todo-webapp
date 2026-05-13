def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters."
    else:
        return None
    
def find_list_by_id(list_id, lists):
    for lst in lists:
        if lst['id'] == list_id:
            return lst
    return None
        
def find_todo_by_id(todo_id, todos):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None

def error_for_todo_name(todo_name):
    if not 1 <= len(todo_name) <= 100:
        return "The todo must be between 1 and 100 characters."
    return None

def delete_todo_by_id(todo_id, todos):
    for idx, todo in enumerate(todos):
        if todo['id'] == todo_id:
            todos.pop(idx)
            return

def mark_all_complete(list):
    for todo in list['todos']:
        todo['completed'] = True
    return None

def delete_list_by_id(list_id, lists):
    for idx, lst in enumerate(lists):
        if lst['id'] == list_id:
            lists.pop(idx)
    return None

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']

def sort_items(items, sort_by):
    sorted_items = sorted(items, key=lambda i: i['title'].lower())
    incomplete_items = [i for i in sorted_items if not sort_by(i)]
    complete_items = [i for i in sorted_items if sort_by(i)]

    return incomplete_items + complete_items