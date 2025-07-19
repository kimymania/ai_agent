import os

from functions.config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        if file_path not in os.path.abspath(full_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        return f"Error: {e}"
