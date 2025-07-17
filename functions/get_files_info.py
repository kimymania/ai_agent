import os


def get_files_info(working_directory, directory="."):
    rel_path = os.path.join(working_directory, directory)
    if working_directory not in os.path.abspath(rel_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(rel_path):
        return f'Error: "{directory}" is not a directory'

    result = ""
    for dir in os.listdir(rel_path):
        full_path = os.path.join(rel_path, dir)
        result += f" - {dir}: file_size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}\n"
    return result
