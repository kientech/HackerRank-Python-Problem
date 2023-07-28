# Solution 01
# import textwrap

# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# Solution 02

def wrap(string, max_width):
    convert_to_list = list(string)
    list_string = []
    character = ""

    for i in convert_to_list:
        if len(character) < max_width:
            character = character + i
        else:
            list_string.append(character)
            character = i
    list_string.append(character)
    return "\n".join(list_string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)













