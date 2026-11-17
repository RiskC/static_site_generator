from enum import Enum
from htmlnode import HTMLNode, LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str , text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("no url or incorrect url")
        return LeafNode("a", text_node.text, {"href":f'{text_node.url}'})
    if text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("no url or incorrect url")
        return LeafNode("img", "", {"src":f'{text_node.url}', "alt":f'{text_node.text}'})
    raise ValueError("Invalid text type:{text_node.type}")
