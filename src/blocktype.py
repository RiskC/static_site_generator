from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block) -> BlockType:

 
    if re.prefixmatch(r"\#{1,6} .+", markdown_block):
        return BlockType.HEADING
    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE

    temp = markdown_block.split("\n")

    if all(t.startswith(">") for t in temp):
        return BlockType.QUOTE
    if all(t.startswith("- ") for t in temp):
        return BlockType.UNORDERED_LIST
    if all(t.startswith(f"{i+1}. ") for i, t in enumerate(temp)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
