import json, dicttoxml
from time import time 


def main():
    input_filename = 'source.json'
    output_filename = 'result.xml'
    with open(input_filename, mode='r', encoding='utf-8') as file:
        json_content = json.loads(file.read())
    with open(output_filename, mode='wb') as file:
        xml_content = dicttoxml.dicttoxml(json_content)
        file.write(xml_content)


if __name__ == '__main__':
    start_time = time()
    for _ in range(10):
        main()
    end_time = time()
    delta_time = end_time - start_time
    print("\nВремя исполнения (с библиотеками):", delta_time)