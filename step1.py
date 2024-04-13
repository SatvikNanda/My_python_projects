#edit and complete and currently running wrong

while True:
    user_action = input("Type add, show, edit,complete, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ") + "\n"

            file = open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\data storage\todos.txt', 'r')

            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\data storage\todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'edit':
            number = int(input("Which number to edit: "))
            number = number-1
            new_todo = input("Enter a new to-do: ")
            todos[number] = new_todo

        case 'show':
            file = open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\data storage\todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos): #for item in todos:
                row = f"{index + 1}.{item}" #f string
                print(row)
        case 'exit':
            break
        case 'complete':
            number = int(input("Index of to-do completed: ")) #when a to-do is completed we remove it from the list
            todos.pop(number - 1)
        case whatever:
            print("please enter the correct command")

print('Bye!')