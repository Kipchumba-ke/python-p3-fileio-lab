def write_file(file_name, file_content):
    #file_name = 'file.txt'
    file_content = "This is a test content."
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)
    pass

def append_file(file_name, append_content):
    #file_name = 'file.txt'
    append_content = "\nAppended content."
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as log_file:
        log_file.write(append_content)
    pass

def read_file(file_name):
    with open(f'{file_name}.txt',mode='r', encoding='utf-8') as text_file:
        content = text_file.read()
        return content
    pass
