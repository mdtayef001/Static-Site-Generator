import re


def extract_markdown_images(text):

    if text == "":
        raise Exception("Invalid text to extract")

    image = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image


def extract_markdown_links(text):

    if text == "":
        raise Exception("Invalid text to extract")
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links
