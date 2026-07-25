import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
            "HTMLNode(p, Hello world, children: None, {'class': 'greeting'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [ParentNode("p", [LeafNode("b", "deep")])],
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><p><b>deep</b></p></section></div>",
        )

    def test_to_html_parent_with_props(self):
        parent_node = ParentNode(
            "div",
            [LeafNode("span", "hi")],
            {"class": "container"},
        )
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>hi</span></div>',
        )

    def test_to_html_no_tag_raises(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children_raises(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()
