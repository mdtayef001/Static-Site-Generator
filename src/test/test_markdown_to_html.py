import unittest
from mardown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading one

### Heading three with **bold**
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><h1>Heading one</h1><h3>Heading three with <b>bold</b></h3></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> that spans two lines
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a quote that spans two lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- first item
- second with **bold**
- third
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>first item</li><li>second with <b>bold</b></li><li>third</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. first item
2. second with _italic_
3. third
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>first item</li><li>second with <i>italic</i></li><li>third</li></ol></div>",
        )

    def test_mixed_document(self):
        md = """
# Title

A paragraph with a [link](https://boot.dev).

- one
- two
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            '<div><h1>Title</h1><p>A paragraph with a <a href="https://boot.dev">link</a>.</p><ul><li>one</li><li>two</li></ul></div>',
        )


if __name__ == "__main__":
    unittest.main()
