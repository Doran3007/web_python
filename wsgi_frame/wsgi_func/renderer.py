def render(template_path):
    with open(template_path) as template_file:
        content = template_file.read()
    return bytes(content, encoding='UTF-8')