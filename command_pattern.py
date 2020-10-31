"""
The command pattern adds a level of abstraction between actions
that must be done,
and the object that invokes those actions,
(normally at a later time)

Command object = implements the action
Invoker object = executes the command at the right time

Eg: In a GUI,
the program could be the receiver object.
a keyboard key may be the invoker object.
The action the key performs (delete, space etc) is the command object interface.

Note: this isn't the most pythonic implementation ever since the
class boilerplate is so similar to each other.
"""

import sys

# Define some receiver classes


class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


# Define some invoker classes


class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


# Define the commands themselves


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


if __name__ == "__main__":
    # Create two receivers
    window = Window()
    document = Document("a_document.txt")

    # Create two commands
    save = SaveCommand(document)
    exit = ExitCommand(window)

    # Create several invokers
    save_button = ToolbarButton('save', 'save.png')
    save_button.command = save
    save_keystroke = KeyboardShortcut("s", "ctrl")
    save_keystroke.command = save
    exit_menu = MenuItem("File", "Exit")
    exit_menu.command = exit
