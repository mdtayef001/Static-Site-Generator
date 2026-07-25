import unittest
from extract_mardown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "![rick](https://i.imgur.com/aaa.png) and ![morty](https://i.imgur.com/bbb.png)"
        )
        self.assertListEqual(
            [
                ("rick", "https://i.imgur.com/aaa.png"),
                ("morty", "https://i.imgur.com/bbb.png"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com"),
            ],
            matches,
        )

    def test_links_ignore_images(self):
        matches = extract_markdown_links(
            "![an image](https://i.imgur.com/aaa.png) and [a link](https://www.boot.dev)"
        )
        self.assertListEqual([("a link", "https://www.boot.dev")], matches)

    def test_images_ignore_links(self):
        matches = extract_markdown_images(
            "![an image](https://i.imgur.com/aaa.png) and [a link](https://www.boot.dev)"
        )
        self.assertListEqual([("an image", "https://i.imgur.com/aaa.png")], matches)

    def test_no_images(self):
        matches = extract_markdown_images("This is plain text with no images")
        self.assertListEqual([], matches)

    def test_no_links(self):
        matches = extract_markdown_links("This is plain text with no links")
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
