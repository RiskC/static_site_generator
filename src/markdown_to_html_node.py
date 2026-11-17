
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

# top level function
def markdown_to_html_node(markdown) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        children.append(director(block_type, block))

    return ParentNode("div", children)

# director function to convert block type into respective html node
def director(block_type, block):
    if block_type == BlockType.PARAGRAPH:
        parent_html_node = convert_paragraph(block)
        return parent_html_node

    if block_type == BlockType.HEADING:
        parent_html_node = convert_headers(block)
        return parent_html_node

    if block_type == BlockType.CODE:
        parent_html_node = convert_code(block)
        return parent_html_node

    if block_type == BlockType.QUOTE:
        parent_html_node = convert_quote(block)
        return parent_html_node

    if block_type == BlockType.UNORDERED_LIST:
        parent_html_node = convert_unordered_lists(block)
        return parent_html_node

    if block_type == BlockType.ORDERED_LIST:
        parent_html_node = convert_ordered_lists(block)
        return parent_html_node



# header helper function to create html node
def convert_headers(block):
    hash_count = block.count("#")
    if hash_count == 1:
        heading_text = block.strip("# ")
        children = text_to_html_children(heading_text)
        return ParentNode("h1", children)
    elif hash_count == 2:
        heading_text = block.strip("## ")
        children = text_to_html_children(heading_text)
        return ParentNode("h2", children)
    elif hash_count == 3:
        heading_text = block.strip("### ")
        children = text_to_html_children(heading_text)
        return ParentNode("h3", children)
    elif hash_count == 4:
        heading_text = block.strip("#### ")
        children = text_to_html_children(heading_text)
        return ParentNode("h4", children)
    elif hash_count == 5:
        heading_text = block.strip("##### ")
        children = text_to_html_children(heading_text)
        return ParentNode("h5", heading_text)
    elif hash_count == 6:
        heading_text = block.strip("###### ")
        children = text_to_html_children(heading_text)
        return ParentNode("h6", children)

#code helper function to create html node
def convert_code(block):
    ticks_stripped = block.strip("`").removeprefix("\n")
    code_node = TextNode(ticks_stripped, TextType.CODE, None)
    children = text_node_to_html_node(code_node)
    return ParentNode("pre", [children])

#quote helper function to create html node
def convert_quote(block):
    temp = block.split("\n")
    stripped = []
    for t in temp:
        stripped.append(t.removeprefix(">").strip())
    clean_text = " ".join(stripped)
    children = text_to_html_children(clean_text)
    return ParentNode("blockquote", children)

#unordered list helpfer function to create html node
def convert_unordered_lists(block):
    temp = block.split("\n")
    children = []
    for t in temp:
        stripped = t.removeprefix("- ")
        child = text_to_html_children(stripped)

        children.append(ParentNode("li", child))
    return ParentNode("ul", children)

#ordered list helper function to create html node
def convert_ordered_lists(block):
    temp = block.split("\n")
    children = []
    for i,t in enumerate(temp):
        stripped = t.removeprefix(f'{i+1}. ')
        child = text_to_html_children(stripped)

        children.append(ParentNode("li", child))
    return ParentNode("ol", children)

# paragraph helper function to create html node
def convert_paragraph(block):
    stripped = block.replace("\n", " ")
    children = text_to_html_children(stripped)
    return ParentNode("p", children)


# helper function to take text -> text node -> HTML node
# this creates leaf nodes which are children html nodes
def text_to_html_children(block):
    children = []
    text_nodes: list = text_to_textnodes(block)
    #text_nodes is a list
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children



# HTML nodes
# HTMLNode(self, tag, value, children, props)


# block types
# 1) paragraph
# 2) heading
# 3) code
# 4) quote
# 5) unordered list
# 6) ordered list

# order of operations:
# 1) markdwon to block (markdown_to_blocks_function)
# 2) block to block types (block_to_block_types function)
# 3) create HTML nodes based on block types (assigning html tags)
# 4) create text nodes from markdown text using (text_to_textnodes)
# 5) create html nodes from text nodes (text_node_to_html_node)
