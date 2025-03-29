from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[ anchor text] (url)"
    IMAGE = "![ alt text ](url)"

    # voila we just used our first enum in python


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    """
        this is a rich comparison function that checks if two instances of the objects have 
        equal properties
        @return :True is all attributes match, otherwise False
    """
    def __eq__(self, other):
        if isInstance(self, other):
            return(
                    self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url
                    )
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

