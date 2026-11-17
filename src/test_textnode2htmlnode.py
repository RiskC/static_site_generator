import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode2HTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_bold(self):
        node = TextNode("This is really bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is really bold text")


    def test_italic(self):
        node = TextNode("Italics are rad", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italics are rad")

    def test_code(self):
        node = TextNode("i love boot.dev", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "i love boot.dev")

    def test_link(self):
        node = TextNode("learn to code here", TextType.LINK, "boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "learn to code here")
        self.assertEqual(html_node.props, {"href":"boot.dev"})

    def test_image(self):
        node = TextNode("this is boots the bear", TextType.IMAGE, "boots the bear")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"boots the bear", "alt":"this is boots the bear"})


    def test_no_link_url(self):
        node = TextNode("learn to code here", TextType.LINK)

        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "no url or incorrect url")

    def test_no_image_url(self):
        node = TextNode("this is boots the bear", TextType.IMAGE)

        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "no url or incorrect url")



if __name__ == "__main__":
    unittest.main()
