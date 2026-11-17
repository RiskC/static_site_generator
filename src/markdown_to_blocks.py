

def markdown_to_blocks(markdown: str) -> list[str]:
    result = []

    temp = markdown.split("\n\n")

    for t in temp:
        if t:
            result.append(t.strip())
    return result
