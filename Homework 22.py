def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    try:
        for index, string in enumerate(strings, start=1):
            byte_position = file.tell()
            file.write(string + '\n')
            strings_positions[(index, byte_position)] = string
    finally:
        file.close()

    return strings_positions


# Пример использования
file_name = 'output.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write(file_name, strings)
print(result)
