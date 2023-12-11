
from colored import fg, attr, bg
from todo_functions import add_todo, remove_todo, mark_todo,view_todo


file_name = "list.csv"

try:
    todo_file = open(file_name, "r")
    todo_file.close()
    print("I am try block")
except FileNotFoundError:
    
    todo_file = open(file_name, "w")
    todo_file.write("title, completed\n")
    todo_file.close()
    print("I am except block")

print(f"{fg('black')}{bg('white')}Welcome to your todo list{attr('reset')}")

def create_menu():
    print("1.Enter 1 to  Add item to your list")
    print("3. Enter 2 to Remove item to your list")
    print("3. Enter 3 to Mark item to your list as completed")
    print("4. Enter 4 to View items in your list ")
    print("5. Enter 5 to exit ")
    choice = input("Enter your selection: ")
    return choice


users_choice = ""

while users_choice != "5":
    users_choice = create_menu()
    if (users_choice =="1"):
        add_todo(file_name)
    elif(users_choice == "2"):
        remove_todo(file_name)
    elif users_choice == "3":
        mark_todo(file_name)
    elif users_choice == "4":
        view_todo(file_name)
    elif users_choice == "5":
        print("exxit")
        continue
    else:
        print("Invalid input")
        
print ("thank you for using to do list")
    
    
