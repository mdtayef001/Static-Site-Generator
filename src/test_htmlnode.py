import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Click me",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello world")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello world", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode("img", None, None, {"src": "image.png"})
        self.assertEqual(node.props_to_html(), ' src="image.png"')

    def test_repr(self):
        node = HTMLNode("p", "Hello world", None, {"class": "greeting"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, Hello world, None, {'class': 'greeting'})",
        )


if __name__ == "__main__":
    unittest.main()
