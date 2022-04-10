import json, dicttoxml


def main():
    input_filename = 'source.json'
    output_filename = 'result.xml'
    with open(input_filename, mode='r', encoding='utf-8') as file:
        json_content = json.loads(file.read())
    with open(output_filename, mode='wb') as file:
        xml_content = dicttoxml.dicttoxml(json_content)
        file.write(xml_content)


if __name__ == '__main__':
    main()