import os, sys

from textnode import TextNode
from htmlnode import HTMLNode

from static_to_public import static_to_public
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
def main():

    if not sys.argv[1]:
        basepath = "/"
    basepath = sys.argv[1]





    static_to_public("./static", "./docs")
    print(os.listdir(os.path.abspath("docs")))

    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == '__main__':
    main()
