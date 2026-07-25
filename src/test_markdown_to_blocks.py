import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_paragraph_list(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_single_block(self):
        self.assertEqual(
            markdown_to_blocks("Just one paragraph"),
            ["Just one paragraph"],
        )

    def test_excessive_newlines(self):
        md = """
First block




Second block
"""
        self.assertEqual(markdown_to_blocks(md), ["First block", "Second block"])

    def test_strips_whitespace(self):
        md = "   Padded block   \n\n   Another one   "
        self.assertEqual(markdown_to_blocks(md), ["Padded block", "Another one"])

    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_only_newlines(self):
        self.assertEqual(markdown_to_blocks("\n\n\n\n"), [])


if __name__ == "__main__":
    unittest.main()
