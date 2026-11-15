from platform import node

from textnode import TextType, TextNode




def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        temp = node.text.split(delimiter)
        
        if len(temp) % 2 == 0:
            raise ValueError("no closing delimiter")


        for i in range(len(temp)):
            if i % 2 == 0:
                if not temp[i]:
                    continue
                result.append(TextNode(temp[i], TextType.TEXT))

            if i % 2 != 0:
                result.append(TextNode(temp[i], text_type))

    return result
    







    #node = TextNode("This is text with a `code block` word", TextType.TEXT)
    #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    #example below
    # node = TextNode("This is text with a 'code block' word", TextType.Text)
    # new_nodes = split_nodes_delimiter([node], "'" TextType.CODE)

    # markdown paragraph has no delimiters, it just goes from text to text
    # markdown bold has the double asterisks around the word (eg **word**)
    # markdown italics has underscores surrounding the word (eg _word_)
    # markdown backtick for code, word is surrounded by back tick on each side (eg `code`)
 
