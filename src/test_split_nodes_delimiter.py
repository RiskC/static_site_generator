from pydoc import splitdoc
from shlex import split
import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode



class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, output)


    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)

        output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_node, output)


    def test_italic(self):
        node = TextNode("It is a _pleasure_ to meet you", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)

        output = [
            TextNode("It is a ", TextType.TEXT),
            TextNode("pleasure", TextType.ITALIC),
            TextNode(" to meet you", TextType.TEXT),
        ]
        self.assertEqual(new_node, output)


    def test_bold_to_code(self):
        node = TextNode("Read **this** and `that`.",TextType.TEXT)
        new_node1 = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_node2 = split_nodes_delimiter(new_node1, "`", TextType.CODE)


        output = [
            TextNode("Read ", TextType.TEXT),
            TextNode("this", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("that", TextType.CODE),
            TextNode(".", TextType.TEXT),

        ]
        self.assertEqual(new_node2, output)


    def test_just_bold(self):
        node = TextNode("**This is just bold**", TextType.BOLD)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)

        output = [
            TextNode("**This is just bold**", TextType.BOLD)
        ]
        self.assertEqual(new_node, output)


    def test_no_closing_delimiter(self):
        node = TextNode("`this code block is missing the closing delimiter", TextType.TEXT)
                
        with self.assertRaises(ValueError) as cm:
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(str(cm.exception), "no closing delimiter")


    def test_double_code(self):
        node = TextNode("this has `two code` blocks `in the` phrase", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)

        output = [
            TextNode("this has ", TextType.TEXT),
            TextNode("two code", TextType.CODE),
            TextNode(" blocks ", TextType.TEXT),
            TextNode("in the", TextType.CODE),
            TextNode(" phrase", TextType.TEXT),

        ]
        self.assertEqual(new_node, output)


    def test_back_to_back_bold(self):
        node = TextNode("**back****back**", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)

        output = [
            TextNode("back", TextType.BOLD),
            TextNode("back", TextType.BOLD),

        ]
        self.assertEqual(new_node, output)



if __name__ == "__main__":
    unittest.main()
