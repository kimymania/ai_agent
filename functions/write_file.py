import os


def write_file(working_directory, file_path, content):
    rel_path = os.path.join(working_directory, file_path)
    if working_directory not in os.path.abspath(rel_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # First, create directory (not actual file) if it doesn't exist
    directory = os.path.dirname(rel_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with open(rel_path, "w", encoding="utf-8") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
