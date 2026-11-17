import re

from textnode import TextNode, TextType

def extract_markdown_images(text):
    #![Description of image](url/of/image.jpg)
    result: list[tuple] = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return result


def extract_markdown_links(text):
    #This is a paragraph with a [link](https://www.google.com).
    result: list[tuples] = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return result

