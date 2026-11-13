from textnode import TextNode
from htmlnode import HTMLNode
def main():
    test_obj = TextNode("hey its me", "bold_text")

    print(test_obj)
    
    test_obj2_kid = HTMLNode("p", "this is a paragraph") 
    test_obj2 = HTMLNode("p", "this is a paragraph", [test_obj2_kid],{"href":"boot.dev"})

    print(test_obj2)

if __name__ == '__main__':
    main()
