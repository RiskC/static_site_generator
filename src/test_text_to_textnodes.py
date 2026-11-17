import unittest

from text_to_textnodes import text_to_textnodes
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_images_links import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestTextToTextNodes(unittest.TestCase):
    def test_1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        new_nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )
    def test_2(self):
        text = "I learned to **code** at [link](www.boot.dev) and I _highly_ recommend it to anyone interested in learning to `code` ![image](happydancing.gif)"
        
        new_nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("I learned to ", TextType.TEXT),
                TextNode("code", TextType.BOLD),
                TextNode(" at ", TextType.TEXT),
                TextNode("link", TextType.LINK, "www.boot.dev"),
                TextNode(" and I ", TextType.TEXT),
                TextNode("highly", TextType.ITALIC),
                TextNode(" recommend it to anyone interested in learning to ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "happydancing.gif"),

            ],
            new_nodes
        )



if __name__ == "__main__":
    unittest.main()

