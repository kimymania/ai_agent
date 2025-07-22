import os
import subprocess


def run_python_file(working_directory, file_path: str, args=[]):
    rel_path = os.path.join(working_directory, file_path)
    if working_directory not in os.path.abspath(rel_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(rel_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        cmd = ["python", rel_path]
        if args:
            for arg in args:
                cmd.append(arg)
        process = subprocess.run(
            cmd,
            timeout=30,
            # capture_output=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    if not process.stdout and not process.stderr:
        return "No output produced"

    stdout = f"STDOUT: {process.stdout}"
    stderr = f"STDERR: {process.stderr}"
    if process.returncode != 0:
        error = f"Process exited with code {process.returncode}"
    else:
        error = ""
    return f"{stdout}\n{stderr}\n{error}"
