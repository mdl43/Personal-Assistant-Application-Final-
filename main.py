import json
from PersonalAssistant import PersonalAssistant

with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)
    
    assistant = PersonalAssistant(todo_list, birthday_list, contact_list)
  
done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays *****      
    4: Get Birthdays
    5: Add Birthday
    6: Remove Birthday
    **** Contacts *****      
    7: Get a Single Contact
    8: Add a Contact
    9: Delete a Contact

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
      #Get Birthday
    elif user_command == "4":
        print("Your birthday contacts:\n")
        for name in assistant.get_birthdays():
          print(name)
        user_input = input("\nEnter a Name: ")
        print(f"\n{assistant.get_birthday(user_input)}")
      #Add Birthday      
    elif user_command == "5":
        name = input("What's your friend's name: ")
        date = input("When's your friend's birth date (ex: 08/18/2000): ")
        print(name)
        print(date)
        assistant.add_birthday(name, date)
        print("\nBirthday Added!")
    elif user_command == "6":
        for name in assistant.get_birthdays():
          print(name)
        user_input = input("Who's name do you want to remove from your list?: ")
        print(f"\n {assistant.remove_birthday(user_input)}")
          # Add Contacts
    elif user_command == "7":
        print("Your contact list:\n")
        for name in assistant.get_contacts():
          print(name)
        user_input = input("\nEnter a Name to See Role: ")
        print(f"\n{assistant.get_contact(user_input)}")
    elif user_command == "8":
        name = input("What's your contact's name: ")
        role = input("When's your contact's role: ")
        print(name)
        print(role)
        assistant.add_contact(name, role)
        print("\nContact Added!")
    elif user_command == "9":
        for name in assistant.get_contacts():
          print(name)
        user_input = input("Who's name do you want to remove from your contact list?: ")
        print(f"\n {assistant.remove_contact(user_input)}")
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
  json.dump(assistant.get_todos(), write_todos)
  json.dump(assistant.get_birthdays(), write_birthdays)
  json.dump(assistant.get_contacts(), write_contacts)