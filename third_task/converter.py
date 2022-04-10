import xml_converter
import json_parser
from time import time


def main():
    input_filename = 'source.json'
    output_filename = 'result.xml'
    with open(input_filename, mode='r') as file:
        content = json_parser.parse(file.read())
    with open(output_filename, mode='w') as file:
        file.write(xml_converter.convert(content))


if __name__ == '__main__':
    start_time = time()
    for _ in range(10):
        main()
    end_time = time()
    delta_time = end_time - start_time
    print("\nВремя исполнения (с регулярками):", delta_time)