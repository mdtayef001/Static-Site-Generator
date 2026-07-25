import unittest
from markdown_to_blocks import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_heading_all_levels(self):
        for hashes in ["#", "##", "###", "####", "#####", "######"]:
            block = f"{hashes} Heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_too_many_hashes(self):
        self.assertEqual(
            block_to_block_type("####### Seven hashes"), BlockType.PARAGRAPH
        )

    def test_heading_no_space(self):
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = "> This is a quote\n> with two lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_broken(self):
        block = "> This is a quote\nbut this line is not"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- first item\n- second item\n- third item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_broken(self):
        block = "- first item\nnot a list item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_no_space(self):
        self.assertEqual(block_to_block_type("-nospace"), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_skipped_number(self):
        block = "1. first\n3. skipped two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_wrong_start(self):
        block = "2. starts at two\n3. then three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is just a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        block = "This is a paragraph\nspanning two lines."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
