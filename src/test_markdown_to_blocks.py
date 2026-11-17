import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
Lorem ipsum dolor sit amet, **consectetur** adipiscing elit. `Integer` sit amet aliquam metus, in ultrices _neque_. 

Sed posuere eu nibh at bibendum. Integer varius faucibus nisl, a malesuada sem aliquam sagittis. Etiam eu venenatis nulla. Nullam aliquam sed tellus a condimentum. Fusce posuere porta magna vel laoreet. Donec porttitor nulla id eros facilisis semper. Curabitur bibendum semper ornare. Vivamus sem diam, ornare at magna lacinia, imperdiet venenatis tellus. Nam id scelerisque nisi, eget efficitur metus. Suspendisse mattis ac libero at tristique. 

- Integer ut sollicitudin nibh. Fusce sollicitudin lorem eget purus gravida bibendum. Aenean vel tincidunt justo. Maecenas sit amet est condimentum est accumsan bibendum
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Lorem ipsum dolor sit amet, **consectetur** adipiscing elit. `Integer` sit amet aliquam metus, in ultrices _neque_.",
                "Sed posuere eu nibh at bibendum. Integer varius faucibus nisl, a malesuada sem aliquam sagittis. Etiam eu venenatis nulla. Nullam aliquam sed tellus a condimentum. Fusce posuere porta magna vel laoreet. Donec porttitor nulla id eros facilisis semper. Curabitur bibendum semper ornare. Vivamus sem diam, ornare at magna lacinia, imperdiet venenatis tellus. Nam id scelerisque nisi, eget efficitur metus. Suspendisse mattis ac libero at tristique.",
                "- Integer ut sollicitudin nibh. Fusce sollicitudin lorem eget purus gravida bibendum. Aenean vel tincidunt justo. Maecenas sit amet est condimentum est accumsan bibendum",

            ],
        )
    def test_markdown_to_blocks3(self):
        md = """
Lorem ipsum dolor sit amet, **consectetur** adipiscing elit. `Integer` sit amet aliquam metus, in ultrices _neque_. 






Sed posuere eu nibh at bibendum. Integer varius faucibus nisl, a malesuada sem aliquam sagittis. Etiam eu venenatis nulla. Nullam aliquam sed tellus a condimentum. Fusce posuere porta magna vel laoreet. Donec porttitor nulla id eros facilisis semper. Curabitur bibendum semper ornare. Vivamus sem diam, ornare at magna lacinia, imperdiet venenatis tellus. Nam id scelerisque nisi, eget efficitur metus. Suspendisse mattis ac libero at tristique. 

- Integer ut sollicitudin nibh. Fusce sollicitudin lorem eget purus gravida bibendum. Aenean vel tincidunt justo. Maecenas sit amet est condimentum est accumsan bibendum
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Lorem ipsum dolor sit amet, **consectetur** adipiscing elit. `Integer` sit amet aliquam metus, in ultrices _neque_.",
                "Sed posuere eu nibh at bibendum. Integer varius faucibus nisl, a malesuada sem aliquam sagittis. Etiam eu venenatis nulla. Nullam aliquam sed tellus a condimentum. Fusce posuere porta magna vel laoreet. Donec porttitor nulla id eros facilisis semper. Curabitur bibendum semper ornare. Vivamus sem diam, ornare at magna lacinia, imperdiet venenatis tellus. Nam id scelerisque nisi, eget efficitur metus. Suspendisse mattis ac libero at tristique.",
                "- Integer ut sollicitudin nibh. Fusce sollicitudin lorem eget purus gravida bibendum. Aenean vel tincidunt justo. Maecenas sit amet est condimentum est accumsan bibendum",

            ],
        )


if __name__ == "__main__":
    unittest.main()
