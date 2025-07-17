import os


def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)
    if path not in os.path.abspath(directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    for file in os.listdir(directory):
        print(
            f"- {file}: file_size={os.path.getsize(file)}, is_dir={os.path.isfile(file)}"
        )


get_files_info(os.getcwd())
