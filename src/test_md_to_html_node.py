import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestMD2HTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
## Why I am Hungry

#### a novel by will
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Why I am Hungry</h2><h4>a novel by will</h4></div>",

        )
    
    def test_quotes(self):
        md = """
> I am hungry 
> because I havent ate since breakfast
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>I am hungry because I havent ate since breakfast</blockquote></div>"

        )

    def test_ordered_list(self):
        md = """
1. beef
2. rice
3. blue razz drink
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>beef</li><li>rice</li><li>blue razz drink</li></ol></div>"
        )

    def test_unordered_list(self):
        md = """
- i
- enjoy
- edm
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>i</li><li>enjoy</li><li>edm</li></ul></div>"

        )
if __name__ == "__main__":
    unittest.main()

