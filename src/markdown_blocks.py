from enum import Enum
from  htmlnode import *
from textnode import text_node_to_html_node, TextNode, TextType
from markdown_to_textnode import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(text: str) -> list:
    """
    Returns the markdown split into blocks like paragraph, heading, lists, etc.
    """
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


def create_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            return heading_to_html(block)
        case BlockType.QUOTE:
            return quote_to_html(block)
        case BlockType.ULIST:
            return ulist_to_html(block)
        case BlockType.OLIST:
            return olist_to_html(block)
        case BlockType.PARAGRAPH:
            return paragraph_to_html(block)
        case BlockType.CODE:
            return code_to_html(block)
        case _:
            raise ValueError("invalid blocktype")


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        node = create_html_node(block)
        children.append(node)
    return ParentNode("div", children, None)
        

def heading_to_html(block: str):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level > len(block):
        raise ValueError(f"incorrect heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def quote_to_html(block: str):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        line_ = line.lstrip(">").strip()
        new_lines.append(line_)
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)



def ulist_to_html(block: str):
    lines = block.split("\n")
    children = []
    for line in lines:
        text = line[2:]
        node = text_to_children(text)
        children.append(ParentNode("li", node))
    return ParentNode("ul", children)
        


def olist_to_html(block: str):
    lines = block.split("\n")
    html_elements = []
    for line in lines:
        parts = line.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_elements.append(ParentNode("li", children))
    return ParentNode("ol", html_elements)


def paragraph_to_html(block: str):
    lines = block.split("\n")
    content = " ".join(lines)
    children = text_to_children(content)
    return ParentNode("p", children)


def code_to_html(block: str):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children