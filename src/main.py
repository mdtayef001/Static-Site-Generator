from textnode import TextType, TextNode
from htmlnode import LeafNode


def main() -> None:

    test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(leaf_node.to_html())


main()
