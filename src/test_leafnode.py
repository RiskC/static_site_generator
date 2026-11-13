import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "BOLD TEXT!")
        self.assertEqual(node.to_html(), "<b>BOLD TEXT!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "italics!")
        self.assertEqual(node.to_html(), "<i>italics!</i>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "this is a code snippet")
        self.assertEqual(node.to_html(), "<code>this is a code snippet</code>")

    def test_leaf_to_html_header(self):
        node = LeafNode("h1", "massive header")
        self.assertEqual(node.to_html(), "<h1>massive header</h1>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "learn to code here!", {"href": "boot.dev"})
        self.assertEqual(node.to_html(),
        '<a href="boot.dev">learn to code here!</a>'
        )


if __name__ == "__main__":
    unittest.main()

