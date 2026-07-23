from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        set_pieces = old_node.text.split(delimiter)
        if len(set_pieces) % 2 == 0:
            raise Exception("invalid markdown, formatted section not closed")
        split_nodes: list[TextNode] = []
        for i, pieces in enumerate(set_pieces):
            if pieces == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text=pieces, text_type=TextType.TEXT))
            else:
                split_nodes.append(TextNode(text=pieces, text_type=text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
