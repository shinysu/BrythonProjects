from browser import document, html

todolist = []

def display_title():
    return html.LABEL("Todo List App", id="title")

def display_form():
    input_item = html.INPUT(type="text", name="item", value="", placeholder="Enter the todo item", id="item")
    add_btn = html.BUTTON("Add", id="addbtn")
    add_btn.bind("click", action)
    return input_item + html.BR() + add_btn

def form_div():
    formdiv = html.DIV(id="formdiv")
    formdiv <= display_form()
    return formdiv + html.BR() + html.BR() + html.BR()

def list_div():
    return html.DIV(Class="todo-list", id="todo-list")

def delete(event):
    item = event.target.id
    todolist.remove(item)
    update_list()

def create_line(item):
    item_name = html.LABEL(item,id="itemtext")
    del_button = html.BUTTON("X", id=item)
    del_button.bind("click", delete)
    return item_name + del_button

def update_list():
    listdiv.clear()
    list_item = (html.LI(create_line(item), Class="todo") for item in todolist)
    print(list_item)
    list = html.UL(list_item)
    listdiv <= list

def action(event):
    item_name = document["item"]
    item = item_name.value
    if item:
        todolist.append(item)
        item_name.value = ""
    update_list()


container = html.DIV(id="container")
innerdiv = html.DIV(id="innerdiv")
innerdiv <= display_title()
innerdiv <= form_div()
listdiv = list_div()
innerdiv <= listdiv
container <= innerdiv
document <= container
