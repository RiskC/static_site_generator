import unittest

from blocktype import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_heading(self):
        markdown_block = "### Fried Cheese"
        block_type = block_to_block_type(markdown_block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        markdown_block = "```\nrecursion and for loops and so much more ```"
        block_type = block_to_block_type(markdown_block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        markdown_block = "> I like chocolate peanut butter icecream"
        block_type = block_to_block_type(markdown_block)

        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        markdown_block = "- cheese\n- steak\n- milkshake"
        block_type = block_to_block_type(markdown_block)

        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        markdown_block = "1. philly cheese steak\n2. large coke\n3. chocolate milkshake"
        block_type = block_to_block_type(markdown_block)

        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        markdown_block = "this lesson i struggled with the most must because i am super tired"
        block_type = block_to_block_type(markdown_block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()



