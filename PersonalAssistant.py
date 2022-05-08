import json

class PersonalAssistant:
  def __init__(self, todos, birthdays, contacts):
    # self.contacts = {}
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There is no contact name"

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays
  
  def get_birthday(self, name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else: 
      print("Can't find a birthday for this person.")

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"{name}'s birthday is already on the list."
    else: 
      self.birthdays[name] = date
      return f"{name}'s birthday has been added."

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday has been removed."
    else:
      print("Birthday is not in list and can't be removed!")

#Contacts Functions

  def get_contacts(self):
    return self.contacts
  
  def get_contact(self, name):
    if name in self.contacts:
      return f"{name}'s role is {self.contacts[name]}."
    else: 
      print("Can't find a contact for this person.")

  def add_contact(self, name, role):
    if name in self.contacts:
      return f"{name}'s contact is already on the list."
    else: 
      self.contacts[name] = role
      return f"{name}'s contact listing has been added."

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"{name}'s contact listing has been removed."
    else:
      print("Contact's ame is not in list and can't be removed!")