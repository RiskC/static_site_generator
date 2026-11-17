from markdown_to_html_node import markdown_to_html_node

node = markdown_to_html_node("![JRR Tolkien sitting](/images/tolkien.png)")
print(node.to_html())
