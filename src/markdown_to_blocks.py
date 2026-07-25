def markdown_to_blocks(markdown) -> list[str]:
    raw_blocks = markdown.split("\n\n")
    blocks: list[str] = []
    for block in raw_blocks:
        stripped: str = block.strip()
        if stripped != "":
            blocks.append(stripped)
    return blocks
