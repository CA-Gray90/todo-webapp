# PEDAC - Delete a todo
P:
- Trash can icons should be clickable, when you click it, it should delete the todo and redraw the page

- deleted todos should not appear on the screen
- issue a flash success message after deleting a todo
- should be able to delete both done and undone todos
- the count of the todos on the `lists` page should update with the amount of todos
- issue a 404 error if requested todo or list does not exist
- update the action to use a relative path (url_for())

Currently, what happens when we click the `delete` button:
- HTML code for delete button and actions:
    <form class="delete"
                action="/lists/{{ lst.id }}/todos/{{ todo.id }}/delete"
                method="post">
            <button type="submit">Delete</button>
    </form>

    - <form>'s allow the submitting of data
    - action is the url path
    - method: POST
    - 

E:
D:
A:
1. Need to set up the route for the `delete` button:
    - /lists/{{ lst.id }}/todos/{{ todo.id }}/delete

2. In the view function, delete the given todo from the list of todos for the given todo list
    - get the index of the given todo using the todo_id
    - remove the element at the found index from the list of todos
    - set session modified to true

3. Final step: Redirect to `list` page
C