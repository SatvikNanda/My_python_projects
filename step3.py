# avoiding redundant code  by using custom functions.

def get_todos():
    with open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\project1_todo_list\data storage\todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")

    
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append('\n' + todo)

        with open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\project1_todo_list\data storage\todos.txt', 'w') as file:
            file.writelines(todos)

    
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = get_todos()

            new_todo = input("Enter a new to-do: ")
            todos[number] = new_todo + '\n'

            with open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\project1_todo_list\data storage\todos.txt', 'w') as file:
                file.writelines(todos)
        
        except ValueError:
            print("Please enter a valid command:")
            continue


    
    elif user_action.startswith('show'):
        todos = get_todos()

        #todo_listcomp = [item.strip('\n') for item in todos] - this is an alternate method to do strip using list comprehension

        for index, item in enumerate(todos): #for item in todos:
            item = item.strip('\n')
            row = f"{index + 1}.{item}" #f string
            print(row)
    
    
    elif user_action.startswith('complete'):
        try:

            number = int(user_action[9:]) #when a to-do is completed we remove it from the list

            todos = get_todos()

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f"Todo {todo_to_remove} was completed and removed from the list."
            print(message)

            with open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\project1_todo_list\data storage\todos.txt', 'w') as file:
                file.writelines(todos)
        
        except IndexError:
            print("Enter a valid index")
            continue
    
    elif user_action.startswith('exit'):
        break
    

    else :
        print("please enter the correct command")

print('Bye!')