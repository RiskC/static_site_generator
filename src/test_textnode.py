import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_URL(self):
        node = TextNode("bootdev is great", TextType.LINK, "boot.dev")
        node2 = TextNode("bootdev is great", TextType.LINK, "boot.dev")
        self.assertEqual(node, node2)

    def test_eq_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        node2 = TextNode("bold text", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_italic(self):
        node = TextNode("italic text", TextType.ITALIC)
        node2 = TextNode("italic text", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq_code(self):
        node = TextNode("this is a snippet of code", TextType.CODE)
        node2 = TextNode("this is a snippet of code", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq_image(self):
        node = TextNode("this is an image", TextType.IMAGE)
        node2= TextNode("this is an image", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("this is the first not equal TEST", TextType.TEXT)
        node2 = TextNode("this ist the first not equal test", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_neq_2(self):
        node = TextNode("this is a code snippet", TextType.CODE)
        node2 = TextNode("this is italic text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq_3(self):
        node = TextNode("this has a url attached", TextType.TEXT, "boot.dev")
        node2 = TextNode("this has a url attached", TextType.TEXT)
        self.assertNotEqual(node, node2)
        







if __name__ == "__main__":
    unittest.main()

