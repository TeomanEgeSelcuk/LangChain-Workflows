import os
from typing import List, Tuple

def save_as_markdown(results: List[Tuple[str, str, dict]], filename: str):
    """
    Saves the results to a Markdown file.

    Args:
        results (list): A list of tuples where each tuple contains the task type, content, and a dictionary.
        filename (str): The name of the output file.
    """
    # Get the directory of the current workspace
    dir_path = os.getcwd()

    # Join the directory path with the relative path to the output file
    file_path = os.path.join(dir_path, 'Input-Output', filename)

    # Open the file specified by 'file_path' in write mode. 'file' is a file object.
    with open(file_path, 'w') as file:
        # Loop through each tuple in the 'results' list.
        for _, _, response_dict in results:
            # Write the title from the response dictionary as a Markdown header to the file.
            file.write(f"### {response_dict['title']}\n")
            # Start a collapsible Markdown details section.
            file.write(f"<details>\n")
            # Write the text from the response dictionary as the summary of the details section.
            file.write(f"<summary>{response_dict['text']}</summary>\n\n")
            # End the details section.
            file.write("</details>\n\n")