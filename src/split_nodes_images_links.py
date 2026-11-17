from textnode import TextNode, TextType
from extract_markdown_images_links import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []

    for node in old_nodes:
        # if not texttype.text, adds as is to result
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        temp = extract_markdown_images(node.text)
        if not temp:
            result.append(node)
            continue
        text = node.text

        for i in range(len(temp)):
            image_text = temp[i][0]
            image_url = temp[i][1]

            chopped = text.split(f'![{image_text}]({image_url})', maxsplit=1)
            if chopped[0]:
                result.append(TextNode(chopped[0], TextType.TEXT))
            result.append(TextNode(image_text, TextType.IMAGE, image_url))
            text = chopped[1]
        if text:
            result.append(TextNode(text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

#This is a paragraph with a [link](https://www.google.com).


    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        temp = extract_markdown_links(node.text)
        if not temp:
            result.append(node)
            continue
        text = node.text

        for i in range(len(temp)):
            link_text = temp[i][0]
            link_url = temp[i][1]

            chopped = text.split(f'[{link_text}]({link_url})', maxsplit = 1)
            if chopped[0]:
                result.append(TextNode(chopped[0], TextType.TEXT))
            result.append(TextNode(link_text, TextType.LINK, link_url))
            text = chopped[1]
        if text:
            result.append(TextNode(text, TextType.TEXT))
    return result
