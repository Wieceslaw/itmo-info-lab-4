import re


def parse_word(pattern: re.Pattern):
    def parse(string: str):
        string = string.strip()
        if re.fullmatch(pattern, string):
            return string.strip('"')
    return parse


def parse_comma_separated_values(string: str):
    in_array = False
    in_object = False
    in_quotes = False
    result = []
    word = ""
    bracket_counter = 0
    brace_counter = 0
    for i, char in enumerate(string):
        if char == '"' and string[i - 1] != '\\':
            in_quotes = not in_quotes
        if not in_quotes:
            if char == '[':
                bracket_counter += 1
            elif char == ']':
                bracket_counter -= 1
            if char == '{':
                brace_counter += 1
            elif char == '}':
                brace_counter -= 1
            in_array = bool(bracket_counter)
            in_object = bool(brace_counter)
            if not in_array and not in_object:
                if char == ',':
                    result.append(word.strip())
                    word = ""
                else:
                    word += char
            else:
                word += char
        else:
            word += char
    else:
        if char == ',':
            raise ValueError("comma can't be last char")
        result.append(word.strip())
    return result


def parse_array(string: str):
    string = string.strip()
    if re.fullmatch('\[.*\]', string):
        string = string[1:-1].strip()
        if len(string):
            values = string
            return [parse_value(element) for element in parse_comma_separated_values(values)]
        else:
            return []


def parse_keyvalue(string: str):
    string = string.strip()
    if re.fullmatch('\".*\"\s*:\s*.+', string):
        mtch = re.search('(^\".*?[^\\\\]\"\s*?:)', string)
        key = mtch[0]
        return (key.rstrip(':').strip('"').strip(), parse_value(string[mtch.end():].strip()))


def parse_comma_separated_keyvalues(string: str):
    return [parse_keyvalue(keyvalue) for keyvalue in parse_comma_separated_values(string)]


def parse_object(string: str):
    string = string.strip()
    if re.fullmatch('\{.*\}', string):
        string = string[1:-1].strip()
        if len(string):
            return {key: value for key, value in parse_comma_separated_keyvalues(string)}
        else:
            return {}


def parse_value(string: str):
    string = string.strip()
    for parser in parsers:
        result = parser(string)
        if result:
            return result


def parse(string: str):
    string = string.replace("\n", "").strip()
    return parse_value(string)


parsers = [
    parse_word(re.compile('^\".*\"$')),
    parse_word(re.compile('\d+(?:\.\d+)?')),
    parse_word(re.compile('true')),
    parse_word(re.compile('false')),
    parse_word(re.compile('null')),
    parse_object,
    parse_array
]


def main():
    print(parse_keyvalue('"s\\"ad::sa\\": : :\\" \\"\\":: "    :    "value"'))


if __name__ == '__main__':
    main()