import unittest
from textnode import TextNode, TextType
from split_nodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_all_types(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_plain_text(self):
        self.assertListEqual(
            text_to_textnodes("Just plain text"),
            [TextNode("Just plain text", TextType.TEXT)],
        )

    def test_bold_only(self):
        self.assertListEqual(
            text_to_textnodes("A **bold** word"),
            [
                TextNode("A ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_italic_only(self):
        self.assertListEqual(
            text_to_textnodes("An _italic_ word"),
            [
                TextNode("An ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_code_only(self):
        self.assertListEqual(
            text_to_textnodes("Use `print()` here"),
            [
                TextNode("Use ", TextType.TEXT),
                TextNode("print()", TextType.CODE),
                TextNode(" here", TextType.TEXT),
            ],
        )

    def test_image_only(self):
        self.assertListEqual(
            text_to_textnodes("![cat](https://img.com/cat.png)"),
            [TextNode("cat", TextType.IMAGE, "https://img.com/cat.png")],
        )

    def test_link_only(self):
        self.assertListEqual(
            text_to_textnodes("[boot dev](https://boot.dev)"),
            [TextNode("boot dev", TextType.LINK, "https://boot.dev")],
        )

    def test_multiple_bold(self):
        self.assertListEqual(
            text_to_textnodes("**one** and **two**"),
            [
                TextNode("one", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.BOLD),
            ],
        )

    def test_bold_and_italic_together(self):
        self.assertListEqual(
            text_to_textnodes("**bold** then _italic_"),
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" then ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
        )

    def test_image_and_link_together(self):
        self.assertListEqual(
            text_to_textnodes(
                "![pic](https://img.com/p.png) and [site](https://boot.dev)"
            ),
            [
                TextNode("pic", TextType.IMAGE, "https://img.com/p.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("site", TextType.LINK, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
