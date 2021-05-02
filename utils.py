
def text_file_writer(file_name, lists):
    with open(f'{file_name}.txt', 'w') as f:
        for item in lists:
            f.write(f"{item}\n")