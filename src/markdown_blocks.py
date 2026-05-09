from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(text):
    sections = text.split("\n\n")
    filtered = []
    for section in sections:
        if section == "":
            continue
        section = section.strip()
        filtered.append(section)
    return filtered

def block_to_block_type(markdown):
    if markdown.startswith("#") and markdown.lstrip("#").startswith(" "):
        return BlockType.HEADING
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    lines = markdown.split("\n")
    quote = True
    ul = True
    ol = True
    for line in lines:
        if not line.startswith(">"):
            quote = False
        if not line.startswith("- "):
            ul = False
        if not (len(line) > 0 and line[0].isnumeric() and line.startswith(f"{line[0]}. ")):
            ol = False
    if quote:
        return BlockType.QUOTE
    elif ul:
        return BlockType.ULIST
    elif ol:
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH

