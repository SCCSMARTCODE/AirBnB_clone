# Airbnb Project

This project is a command-line interface (CLI) tool for managing properties and bookings in an Airbnb-like system. It provides functionality to create, update, and delete properties, as well as book properties for specific dates.

## Command Interpreter

The command interpreter is a Python-based CLI tool that allows you to interact with the Airbnb system. It provides a set of commands that you can use to perform various operations on properties and bookings.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:

   ```bash
   python airbnb_cli.py

the command line startup chat

create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
If the class name is missing, print ** class name missing ** (ex: $ create)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ show)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ destroy)
If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
The printed result must be a list of strings (like the example below)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
Usage: update <class name> <id> <attribute name> "<attribute value>"
Only one attribute can be updated at the time
You can assume the attribute name is valid (exists for this model)
The attribute value must be casted to the attribute type
If the class name is missing, print ** class name missing ** (ex: $ update)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
Let’s add some rules:

You can assume arguments are always in the right order
Each arguments are separated by a space
A string argument with a space must be between double quote
The error management starts from the first argument to the last one
