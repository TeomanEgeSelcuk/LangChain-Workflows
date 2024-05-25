import re # Import the regular expressions module
from typing import List, Tuple 
import os

def read_input(filename: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
        filename (str): The path to the input file.

    Returns:
        str: The content of the file as a string.
    """
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Join the directory path with the relative path to the input file
    file_path = os.path.join(dir_path, '../Input-Output', filename)

    with open(file_path, 'r') as file:  # Open the file in read mode
        return file.read()  # Read the content of the file and return it

def process_input(input_text: str) -> List[Tuple[str, str]]:

    """
    Transforms the input text into a list of tasks.

    This function takes a string of text as input, where tasks are separated by '---' on a new line.
    If the input text is empty or contains only whitespace, an empty list is returned. 
    Each task consists of a task type and content, separated by a newline. 
    The task type is optional and if not provided, a default task type is assigned. Goes like 'Summarize 1', 'Summarize 2', etc.
    The task type can be specified using a markdown header (e.g., '# Quiz'). 
    The content of the task follows the task type and extends to the end of the task section or until another markdown header is encountered.

    Args:
        input_text (str): The input text containing tasks.

    Returns:
        list: A list of tuples where each tuple contains a task type and content. 
                The task type is a string and the content is also a string.
    """
    if not input_text.strip():  # Check if input_text is empty or contains only whitespace
        return []  # Return an empty list

    sections = input_text.strip().split('\n---\n')  # Split input into sections
    tasks = []  # Initialize task list
    default_task_count = 1  # Counter for default task names

    for section in sections:  # Loop through sections
        parts = section.split('\n', 1)  # Split section into parts
        if len(parts) == 2:  # If section has two parts
            task_type, content = parts  # Unpack parts
            header_match = re.match(r'^(#+)\s*(.+)', task_type.strip())  # Match markdown headers
            if header_match:  # If header is found
                task_type = header_match.group(2).strip()  # Extract task type
            else:  # If no header
                task_type = f'Summarize {default_task_count}'  # Use default task name
                default_task_count += 1  # Increment counter
            content = content.strip()  # Strip content
        else:  # If section has one part
            task_type = parts[0].strip()  # Strip task type
            header_match = re.match(r'^(#+)\s*(.+)', task_type)  # Match markdown headers
            if header_match:  # If header is found
                task_type = header_match.group(2).strip()  # Extract task type
                content = ''  # Set content to empty
            else:  # If no header
                content = task_type  # Use task type as content
                task_type = f'Summarize {default_task_count}'  # Use default task name
                default_task_count += 1  # Increment counter
        tasks.append((task_type, content))  # Add task to list

    return tasks  # Return task list