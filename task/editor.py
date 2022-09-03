available_formatters = ('plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list')
available_commands = ('!help', '!done')


# TODO: cuando se añade texto, ¿añadir un espacio en blanco para separar?
def header(accumulated_text):
    level = int(input('Level: '))
    if level < 1 or level > 6:
        print('The level should be within the range of 1 to 6')
        header(accumulated_text)
    else:
        text = input('Text: ')
        formatted_text = '#' * level + ' ' + text
        if accumulated_text == '':
            accumulated_text = formatted_text + '\n'
        else:
            accumulated_text += '\n' + formatted_text + '\n'
        print(accumulated_text)
    return accumulated_text


def plain(accumulated_text):
    text = input('Text: ')
    accumulated_text += text
    print(accumulated_text)
    return accumulated_text


def bold(accumulated_text):
    text = input('Text: ')
    formatted_text = '**' + text + '**'
    accumulated_text += formatted_text
    print(accumulated_text)
    return accumulated_text


def italic(accumulated_text):
    text = input('Text: ')
    formatted_text = '*' + text + '*'
    accumulated_text += formatted_text
    print(accumulated_text)
    return accumulated_text


def inline_code(accumulated_text):
    text = input('Text: ')
    formatted_text = '`' + text + '`'
    accumulated_text += formatted_text
    print(accumulated_text)
    return accumulated_text


def new_line(accumulated_text):  # revisar
    accumulated_text += '\n'
    print(accumulated_text)
    return accumulated_text


def link(accumulated_text):
    label = input('Label: ')
    url = input('URL: ')
    my_link = '[' + label + ']' + '(' + url + ')'
    accumulated_text += my_link
    print(accumulated_text)
    return accumulated_text


def mk_list(accumulated_text, type):
    nrows = int(input('Number of rows: '))
    if nrows <= 0:
        print('The number of rows should be greater than zero')
        return mk_list(accumulated_text, type)
    else:
        for i in range(nrows):
            counter = str(i + 1)
            message = 'Row #' + counter + ' '
            element = input(message)
            formatted_element = counter + '. ' + element if type == 'ordered-list' else '- ' + element
            accumulated_text += formatted_element + '\n'
        print(accumulated_text)
        return accumulated_text


def markdown(format, general_text):
    match format:
        case 'plain':
            general_text = plain(general_text)
        case 'bold':
            general_text = bold(general_text)
        case 'italic':
            general_text = italic(general_text)
        case 'inline-code':
            general_text = inline_code(general_text)
        case 'link':
            general_text = link(general_text)
        case 'header':
            general_text = header(general_text)
        case 'new-line':
            general_text = new_line(general_text)
        case 'ordered-list':
            general_text = mk_list(general_text, 'ordered-list')
        case 'unordered-list':
            general_text = mk_list(general_text, 'unordered-list')
    return general_text


def interactive(general_text):
    input_formatter = input('Choose a formatter:')
    if input_formatter in available_formatters:
        general_text = markdown(input_formatter, general_text)
        interactive(general_text)
    elif input_formatter == '!help':
        print('Available formatters:', *available_formatters)
        print('Special commands:', *available_commands)
        interactive(general_text)
    elif input_formatter == '!done':
        with open('output.md', 'w') as f:
            print(type(general_text))
            f.write(general_text)
    else:
        print('Unknown formatting type or command')
        interactive(general_text)


def main():
    general_text = ''
    interactive(general_text)


main()
