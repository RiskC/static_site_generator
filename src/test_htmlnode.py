import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    test_self_props = {
    "href": "https://www.google.com",
    "target": "_blank",
    }

    test_children = [HTMLNode("p", "paragraph text")]

    def test_props_to_html(self):
        test_children = [HTMLNode("p", "paragraph text")]
        test_self_props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        html_instance = HTMLNode("p", "this is a paragraph", test_children, test_self_props)

        method_check = html_instance.props_to_html()
        answer =' href="https://www.google.com" target="_blank"'

        self.assertEqual(method_check, answer)

    def test_repr(self):
        node = HTMLNode("p", "this is a paragraph")
        repr_check = node.__repr__()
        answer = "HTMLNode(p, this is a paragraph, None, None)"
        self.assertEqual(repr_check, answer)

    def test_values(self):
        node = HTMLNode("p", "this is a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "this is a paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


if __name__ == "__main__":
    unittest.main()
