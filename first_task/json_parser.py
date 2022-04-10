def parse_string(string: str):
    string = string.strip()
    if len(string) >= 2:
        if string[0] == '"' and string[-1] == '"':
            return string.strip('"')
    return


def parse_number(string: str):
    string = string.strip()
    if len(string) > 0:
        try:
            number = eval(string)
            if type(number) in (int, float):
                return number
        except Exception:
            return


def parse_true(string: str):
    string = string.strip()
    if string == "true":
        return True


def parse_false(string: str):
    string = string.strip()
    if string == "false":
        return False


def parse_null(string: str):
    string = string.strip()
    if string == "null":
        return None


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
    if len(string) >= 2:
        if string[0] == '[' and string[-1] == ']':
            string = string[1:-1].strip()
            if len(string):
                values = string
                return [parse_value(element) for element in parse_comma_separated_values(values)]
            else:
                return []


def parse_keyvalue(string: str):
    string = string.strip()
    if len(string) >= 2:
        if string[0] == '"':     
            key = ""
            for i, char in enumerate(string[1:]):
                if char == '"' and string[i - 1] != '\\':
                    break
                key += char
            else:
                raise ValueError('keyvalue error')
            return (parse_string('"' + key + '"'), parse_value(string[i + 2:].lstrip(':')))
    print(string)


def parse_comma_separated_keyvalues(string: str):
    return [parse_keyvalue(keyvalue) for keyvalue in parse_comma_separated_values(string)]


def parse_object(string: str):
    string = string.strip()
    if len(string) >= 2:
        if string[0] == '{' and string[-1] == '}':
            string = string[1:-1].strip()
            if len(string):
                return {key: value for key, value in parse_comma_separated_keyvalues(string)}
            else:
                return {}


def parse_value(string: str):
    string = string.strip()
    parsers = [
        parse_string,
        parse_number,
        parse_object,
        parse_array,
        parse_true,
        parse_false,
        parse_null
    ]
    for parser in parsers:
        result = parser(string)
        if result:
            return result


def parse(string: str):
    string = string.replace("\n", "").strip()
    return parse_value(string)