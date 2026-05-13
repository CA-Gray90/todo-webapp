# PEDAC - Toggle todo completion status
P:
- The checkboxes beside each todo should be clickable
- Clicking an empty checkbox marks it as done, clicking a checked box marks it undone
- Clicking a box causes the screen to redraw automatically
- Completed todos should have a checkmark, uncompleted do not
- Completed todos will be grayed out
- Flash message confirming success of marking todo as complete

- hook up the checkboxes to respond to clicks and toggle the completion status

- Issue a 404 status code if the requested todo list or specified todo does not exist

E:
D:
A:
What happens when we currently click a checkbox:
    - displaying the `list.html` page, on the '/lists/<list_id>' route
    - We have the following html code for the completed checkbox:
        <form action="/lists/{{ lst.id }}/todos/{{ todo.id }}/toggle"
                method="post" class="check">
            <input type="hidden" name="completed"
                  value="{{ not todo.completed }}" />
            <button type="submit">Complete</button>
          </form>
    
    - action: specifies the route
    - method: post (we are submitting a form)
    - name of the input: 'completed'
    - value (what gets sent in the form): {{ not todo.completed }}

    - 'todo' is a dictionary:
        {'id'   : str(uuid4()),
         'title' : todo,
         'completed' : False}

    - value for 'completed' is a boolean

    When we click the button, we go to the route specified by 'action' with the method: POST
    The input sent is: completed={{ not todo.completed }}
        - If the todo is marked as NOT complete, sends completed=True, else completed=False
    
    currently displays a 404 error

1. Set up the route
    - route: /lists/{{ lst.id }}/todos/{{ todo.id }}/toggle
    - method: POST

2. Check the value of the specified todo.complete to posted value
    - get the value of 'completed' from the request object
        - request.form['completed'] returns the value of 'completed' from the submitted form

    - set the value of todo['completed'] to the value of 'complete' (in the request object)
        - find the todo (helper):
            - given a list of todos with the given data structure:
                {'id'   : str(uuid4()),
                'title' : todo,
                'completed' : False}

            - find the todo of the given ID

            > loop through the todo dicts:
                - check the value of 'id' against given todo_id:
                    - if equal, return todo
            - return None

    - redirect to list.html

3. Flash message saying todo has been marked complete

C