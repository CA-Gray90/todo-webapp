# PEDAC - Mark all todos complete
P:
The complete all button should maark all the todos as complete. This should not be reversible unless you 
individually mark each todo as complete.

- When you click `Complete All` the screen should automatically redraw itself
- All todos should be marked as done
- Issuse a flash success message after clicking `Complete All` : 'All todos have been completed.'

- issue a 404 status code if the list is not found

HTML code for complete button:
    <form class="complete_all"
            action="/lists/{{ lst.id }}/complete_all"
            method="post">
        <button class="check" type="submit">Complete All</button>
    </form>

- action: URL route that the form will trigger
- method: POST


E:
D:
A:
1. Create the route for: `/lists/{{ list.id }}/complete_all`
    
2. Set all todos in the current list as complete

3. Redirect to the `lists.html` page

C