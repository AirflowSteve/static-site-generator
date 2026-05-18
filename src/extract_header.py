def extract_title(markdown: str) -> str:
    """
    This function looks for h1 header in a markdown text and returns it without the '#' tag
    """
    lines = markdown.split("\n")
    for line in lines:
        line = line.lstrip()
        if line.startswith("# "):
            line = line.lstrip("#").lstrip()
            return line
    raise ValueError("no title")