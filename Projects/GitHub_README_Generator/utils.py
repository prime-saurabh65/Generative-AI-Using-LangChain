def convert_list_to_bullets(text):
    lines = text.split(",")

    return "\n".join(
        f"- {line.strip()}"
        for line in lines
        if line.strip()
    )