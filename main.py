import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_functions import available_functions
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        verbose = True
    else:
        verbose = False

    try:
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
    except IndexError as e:
        print(f"{e}: No prompt provided")
        sys.exit(1)

    for _ in range(20):
        try:
            response = generate_content(client, messages, verbose)
            if response.text and not response.function_calls:
                print("Final response:\n", response.text)
                break
        except Exception as e:
            print(f"Error: {e}")


def generate_content(client: genai.Client, messages: list, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    for candidate in response.candidates:
        messages.append(candidate.content)
    if response.function_calls:
        call_functions(response, messages, verbose)
    return response


def call_functions(response, messages: list, verbose):
    """Only call functions and append to messages list"""
    function_call_result = call_function(response.function_calls[0], verbose)

    if not function_call_result.parts[0].function_response.response:
        raise Exception("No response from function call")
    if verbose:
        print(f"-> {function_call_result.parts[0].function_response.response}")

    messages.append(function_call_result)


def call_function(function_call: types.FunctionCall, verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    if function_call.name:
        function_name = function_call.name
    if function_call.args:
        kwargs = function_call.args
    else:
        kwargs = {}

    functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    try:
        run_func = functions[function_name]
        result = run_func("calculator", **kwargs)
    except KeyError:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )


if __name__ == "__main__":
    main()
