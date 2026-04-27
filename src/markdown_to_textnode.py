from textnode import TextType, TextNode

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
    