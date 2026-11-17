import os

from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')


    from_abs_path = os.path.abspath(from_path)
    dest_abs_path = os.path.abspath(dest_path)
    template_abs_path = os.path.abspath(template_path)

    with open(from_abs_path, mode="r") as f:
        md_file = f.read()

    with open(template_abs_path, mode="r") as f:
        template_file = f.read()

    # convert md to node
    node = markdown_to_html_node(md_file)
    # convert node to html with method
    html = node.to_html()

    #take md and grab h1 title
    title = extract_title(md_file)

    #update template with title and content vars
    template_file = template_file.replace("{{ Title }}" , title)
    template_file = template_file.replace("{{ Content }}", html)
    template_file = template_file.replace('href="/', f'href="{basepath}')
    template_file = template_file.replace('src="/', f'src="{basepath}')

    #check to see if dest path exists before write
    if os.path.exists(dest_abs_path) == False:
        #mnakes dirs if they dont exist
        os.makedirs(os.path.dirname(dest_abs_path), exist_ok = True)
    with open(dest_abs_path, mode="w") as f:
        f.write(template_file)
