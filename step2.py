#goal: we will add ifelse conditions and dictionaries
#changes: after add in the same line write what to add
# after edit or complete in the same line give the index number you want to edit or complete



while True:
    user_action = input("Type add, show, edit, complete, or exit: ")

    
    if 'add' in user_action:
        todo = user_action[4:]

        with open(r'..\data storage\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append('\n' + todo)

        with open(r'..\data storage\todos.txt', 'w') as file:
            file.writelines(todos)

    
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number-1

        with open(r'..\data storage\todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter a new to-do: ")
        todos[number] = new_todo + '\n'

        with open(r'..\data storage\todos.txt', 'w') as file:
            file.writelines(todos)

    
    elif 'show' in user_action:
        with open(r'..\data storage\todos.txt', 'r') as file:
            todos = file.readlines()

        #todo_listcomp = [item.strip('\n') for item in todos] - this is an alternate method to do strip using list comprehension

        for index, item in enumerate(todos): #for item in todos:
            item = item.strip('\n')
            row = f"{index + 1}.{item}" #f string
            print(row)
    
    
    elif 'complete' in user_action:
        number = int(user_action[9:]) #when a to-do is completed we remove it from the list

        with open(r'..\data storage\todos.txt', 'r') as file:
            todos = file.readlines()

        index = number-1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        message = f"Todo {todo_to_remove} was completed and removed from the list."
        print(message)

        with open(r'..\data storage\todos.txt', 'w') as file:
            file.writelines(todos)
    
    elif 'exit' in user_action:
        break
    

    else :
        print("please enter the correct command")

print('Bye!')