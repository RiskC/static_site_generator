import unittest

from split_nodes_images_links import split_nodes_image, split_nodes_link
from extract_markdown_images_links import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


class TestSplitImagesLinksNode(unittest.TestCase):
    def test_split_two_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    def test_split_two_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [link](https://www.boot.dev/traininggrounds)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev/traininggrounds"),
            ],
            new_nodes,
        )
    def test_split_three_links(self):
        node = TextNode(
            "This is where i learned to code [link](https://www.boot.dev), this is a helpful resource [python](docs.python.org), and this is whats next[c programming](devdocs.io/c/)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is where i learned to code ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(", this is a helpful resource ", TextType.TEXT),
                TextNode("python", TextType.LINK, "docs.python.org"),
                TextNode(", and this is whats next", TextType.TEXT),
                TextNode("c programming", TextType.LINK, "devdocs.io/c/"),

            ],
            new_nodes
        )
    
    def test_split_three_images(self):
        node = TextNode(
            "my face when they say to write lots of test ![image](dwightscreaming.gif) and my face after a few tests ![gif](stewieinastraightjacket.gif) and ive been writing tests this whole project ![gif](charlieandstringboard.gif)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("my face when they say to write lots of test ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "dwightscreaming.gif"),
                TextNode(" and my face after a few tests ", TextType.TEXT),
                TextNode("gif", TextType.IMAGE, "stewieinastraightjacket.gif"),
                TextNode(" and ive been writing tests this whole project ", TextType.TEXT),
                TextNode("gif", TextType.IMAGE, "charlieandstringboard.gif"),
            ],
            new_nodes

        )

    def test_just_image(self):
        node = TextNode(
            "![image](monkeyslamminglaptop.gif)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "monkeyslamminglaptop.gif"),
            ], 
            new_nodes

        )

    def test_just_link(self):
        node = TextNode(
            "[where i learned to code](www.boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("where i learned to code", TextType.LINK, "www.boot.dev"),
            ],
            new_nodes

        )





if __name__ == "__main__":
    unittest.main()



