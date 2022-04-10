def convert_to_xml(content):
    if type(content) == list:
        return ''.join([f"<element>{convert_to_xml(el)}</element>" for el in content])
    elif type(content) == dict:
        return ''.join([f"<{key}>{convert_to_xml(content[key])}</{key}>" for key in content.keys()])
    elif content is None:
        return ''
    return str(content)


def convert(content):
    if len(content) == 1:
        return '<?xml version="1.0" encoding="UTF-8" ?>' + convert_to_xml(content)
    else:
        return '<?xml version="1.0" encoding="UTF-8" ?>' + '<root>' + convert_to_xml(content) + '</root>'  