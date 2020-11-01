"""
The composite pattern allows complex tree-like structures
to be built from simple components.

These components, called composite objects, are able to behave
sort of like a container and sort of like a variable depending
on whether they have child components.

Composite objects are container objects, where the content may
actually be another composite object.


The composite pattern is commonly useful in
file/folder-like trees.

- The folder is the composite object.
- For each folder, we maintain a dictionary of children.
"""


class Component:
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]

    def __repr__(self):
        return self.name


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child

    def copy(self, new_path):
        pass


class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
        pass


root = Folder('')


def get_path(path):
    names = path.split('/')[1:]
    node = root

    for i, name in enumerate(names):
        node = node.children[name]

    return node


# Create some folders
folder1 = Folder('folder1')
folder2 = Folder('folder2')

# Add them to the root directory
root.add_child(folder1)
root.add_child(folder2)

# Create a child for folder1
folder11 = Folder('folder11')
folder1.add_child(folder11)

# Create a child for folder11
file111 = File('file111', 'contents')
folder11.add_child(file111)

# Create a child for folder2
file21 = File('file21', 'other contents')
folder2.add_child(file21)

# Move folder2 to folder11
folder2.move('/folder1/folder11')
print(folder11.children)

# Move folder21 to folder1
file21.move('/folder1')
print(folder1.children)
