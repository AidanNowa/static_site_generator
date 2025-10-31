from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(headings):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    splits = block.split("\n")
    quote_counter = 0
    unordered_list_counter = 0
    ordered_list_counter = 0
    for split in splits:
        #print(f"split is: {split}")
        if split.startswith(">"):
            quote_counter += 1
        if split.startswith("- "):
            unordered_list_counter += 1
        if re.match(r"\d+\. ", split):
            ordered_list_counter += 1
    if quote_counter == len(splits):
        return BlockType.QUOTE
    if unordered_list_counter == len(splits):
        return BlockType.UNORDERED_LIST
    if ordered_list_counter == len(splits):
        return BlockType.ORDERED_LIST 
    
    return BlockType.PARAGRAPH    
