import csv

def add_todo(file_name):
    print("add todo")
    
    todo_name = input("Enter a todo: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])
    
def remove_todo(file_name):
    print("remove todo")
    
def mark_todo(file_name):
    print("mark todo")
    
def view_todo(file_name):
    print("view todo")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if (row[1] == "True"):
                print(f"Todo {row[0]} is completed")
            else:
                print(f"Todo {row[0]} is not complete")
    
