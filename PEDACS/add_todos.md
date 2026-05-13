# PEDAC
P:
Create a new todo.

The todo gets created and then added to the current todo list when you submit the form. Your program should exhibit the following behaviors:

    When you submit the form, the screen should automatically redraw itself.
    If you enter a valid title for the new todo, the new todo should appear in the list of todos. The new todo should not be marked as completed.
    Issue a flash success message after successfully creating a new todo.
    The todo title is required; issue an appropriate flash error message if the title is unspecified.
    The todo title has a maximum size of 100 characters; display an appropriate flash error when the title is too long. Make sure the invalid title doesn't disappear when the page is redrawn.
    Duplicate todo titles are permitted.
    In the list of todo lists at http://localhost:5003/lists (or port 8080 for Cloud9), the modified todo list should show the new counts.
    Make sure your code issues a 404 status code if the requested todo list does not exist.


