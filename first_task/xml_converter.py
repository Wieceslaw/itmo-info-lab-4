def convert_to_xml(content):
    if type(content) == list:
        return ''.join([f"<element>{convert_to_xml(el)}</element>" for el in content])
    elif type(content) == dict:
        return ''.join([f"<{key}>{convert_to_xml(content[key])}</{key}>" for key in content.keys()])
    elif content is None:
        return ''
    return str(content)


def convert(content):
    return '<?xml version="1.0" encoding="UTF-8" ?>' + '<root>' + convert_to_xml(content) + '</root>'


def main():
    content = {"ad": 2, "vall": {"key": "value", "array": [1, 2, 3]}}
    print(convert(content))


if __name__ == '__main__':
    main()