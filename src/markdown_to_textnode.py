from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("haven't found a closing delimiter")
            nodes = node.text.split(delimiter)
            for i in range(len(nodes)):
                if nodes[i]:
                    if i % 2 == 0:
                        new_list.append(TextNode(nodes[i], TextType.TEXT))
                    else:
                        new_list.append(TextNode(nodes[i], text_type))
        
    return new_list

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            original_text = node.text
            images = extract_markdown_images(original_text)
            if len(images) == 0:
                new_list.append(node)
                continue
            for image in images:
                sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                if sections[0] != "":
                    new_list.append(TextNode(sections[0], TextType.TEXT))
                new_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
                original_text = sections[1]
            if original_text != "":
                new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            original_text = node.text
            links = extract_markdown_links(original_text)
            if len(links) == 0:
                new_list.append(node)
                continue
            for link in links:
                sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                if sections[0] != "":
                    new_list.append(TextNode(sections[0], TextType.TEXT))
                new_list.append(TextNode(link[0], TextType.LINK, link[1]))
                original_text = sections[1]
            if original_text != "":
                new_list.append(TextNode(original_text, TextType.TEXT))
                
    return new_list


def extract_markdown_images(text):
    found_alt = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return found_alt

def extract_markdown_links(text):
    alt_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_text

def text_to_textnodes(text):
    text_to_work = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(text_to_work, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
