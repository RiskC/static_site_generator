import os

from textnode import TextNode
from htmlnode import HTMLNode

from static_to_public import static_to_public

def main():
    static_to_public("static", "public")
    print(os.listdir(os.path.abspath("public")))
    
if __name__ == '__main__':
    main()
