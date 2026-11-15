import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


    def test_no_tag_test(self):
        node = LeafNode("p", "paragraph text")
        node2 = ParentNode("", [node])
        
        with self.assertRaises(ValueError) as cm:
            node2.to_html()
        self.assertEqual(str(cm.exception), "Parent node does not have a tag")


    def test_no_children_test(self):
        node = ParentNode("p", [])

        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "Parent node has no children; children required for parent node")


    def test_children(self):
        node1 = LeafNode("b", "I")
        node2 = LeafNode("b", "want")
        node3 = LeafNode("b", "chocolate")
        node4 = LeafNode("b", "chip")
        node5 = LeafNode("b", "pancakes")
        node6 = ParentNode("p", [node1, node2, node3, node4, node5])
        self.assertEqual(node6.to_html(), "<p><b>I</b><b>want</b><b>chocolate</b><b>chip</b><b>pancakes</b></p>")


    def test_children_nest(self):
        node1 = LeafNode("i", "I")
        node2 = LeafNode("i", "want")
        node3 = LeafNode("i", "chocolate")
        node4 = LeafNode("i", "chip")
        node5 = LeafNode("i", "pancakes")
        node6 = ParentNode("p", [node1, node2, node3, node4, node5])
        node7 = LeafNode("h1", "My request is stated below")
        node8 = LeafNode("h3", "and I want it now, no objections")
        node9 = ParentNode("b", [node7, node8, node6])
        self.assertEqual(
            node9.to_html(), 
            "<b><h1>My request is stated below</h1><h3>and I want it now, no objections</h3><p><i>I</i><i>want</i><i>chocolate</i><i>chip</i><i>pancakes</i></p></b>"
        )


    def test_self_props(self):
        node1 = LeafNode("a", "this is where i got cracked at coding", {"href":"boot.dev"})
        node2 = ParentNode("i", [node1])
        node3 = LeafNode("h1", "what taught me to code is below")
        node4 = ParentNode("b", [node3, node2])
        self.assertEqual(
        node4.to_html(),
            '<b><h1>what taught me to code is below</h1><i><a href="boot.dev">this is where i got cracked at coding</a></i></b>'

        )





if __name__ == "__main__":
    unittest.main()
