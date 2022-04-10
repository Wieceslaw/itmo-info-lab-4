import xml_converter
import json_parser


def main():
    input_filename = 'source.json'
    output_filename = 'result.xml'
    with open(input_filename, mode='r') as file:
        content = json_parser.parse(file.read())
    with open(output_filename, mode='w') as file:
        file.write(xml_converter.convert(content))


if __name__ == '__main__':
    main()