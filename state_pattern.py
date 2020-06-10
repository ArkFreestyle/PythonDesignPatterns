"""
The state pattern is similar to the strategy pattern structure-wise, but its intent is different.
The goal of the state pattern is to represent state-transition systems.

State-transition systems are systems where it is obvious that an object can be in a specific state,
and that certain activities could change its state.

So for this we have:
1) A context class
    - A manager that provides an interface for switching states.
    - Maintains the current state.
    - Forwards actions to the state classes.
2) Multiple state classes
    - A black box which performs state management internally.

We'll build a simple XML parser to illustrate this pattern.

"""

xml_to_parse = \
"""
<book>
    <author>Dusty Phillips</author>
    <publisher>Packt Publishing</publisher>
    <title>Python 3 Object Oriented Programming</title>
    <content>
        <chapter>
            <number>1</number>
            <title>Object Oriented Design</title>
        </chapter>
        <chapter>
            <number>2</number>
            <title>Objects In Python</title>
        </chapter>
    </content>
</book>
"""


class Node:
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        else:
            return self.tag_name


class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None
        self.state = FirstTag()
    
    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)
    
    def start(self):
        self.process(self.parse_string)


class FirstTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        tag_name = remaining_string[i_start_tag+1:i_end_tag]
        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode()
        return remaining_string[i_end_tag+1:]


class ChildNode:
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        
        if stripped.startswith("</"):
            parser.state = CloseTag()
        
        elif stripped.startswith("<"):
            parser.state = OpenTag()
        
        else:
            parser.state = TextNode()
        
        return stripped


class OpenTag:
    pass


class CloseTag:
    pass


class TextNode:
    pass
