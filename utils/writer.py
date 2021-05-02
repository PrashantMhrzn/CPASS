import os


def text_file_writer(master, first_name):
    dirs = os.listdir()

    if first_name+'.txt' in dirs:
        first_name = f'{first_name}-{len(dirs)}'

    with open(f'{first_name}.txt', 'w') as f:
        for item in master:
            f.write(f"{item}\n")
