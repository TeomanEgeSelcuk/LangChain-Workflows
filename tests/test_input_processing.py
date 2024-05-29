import pytest
import os 
from langchain_env.input_processing import read_input, process_input
from langchain_env.file_operations import save_as_markdown

def test_read_input():
    # Define the expected results
    results = [
        ("Summarize", "This is task 1 content", {"title": "Task 1 Title", "text": "Task 1 Summary"})
    ]

    # Define the filename for the test file
    filename = "test_reading_input.md"
    
    # Save the results to a markdown file
    save_as_markdown(results, filename)

    # Get the current working directory
    dir_path = os.getcwd()
    
    # Construct the full path to the test file
    file_path = os.path.join(dir_path, 'Input-Output', filename)

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Read the input from a test file (assuming it exists in the Input-Output directory)
    content = read_input('input.md')
    
    # Assert that the read_input function returns a string
    assert isinstance(content, str), "read_input should return a string"

    # Remove the test file after the test
    os.remove(file_path)

def test_process_input():
    # Test with only task types, no content
    input_text = "# First Task\n---\n### Second Task"
    tasks = process_input(input_text)
    assert isinstance(tasks, list), "process_input should return a list"
    assert len(tasks) == 2, "process_input should return a list of two tasks"
    assert tasks[0] == ('First Task', ''), "First task should be ('First Task', '')"
    assert tasks[1] == ('Second Task', ''), "Second task should be ('Second Task', '')"

    # Test with task types and content
    input_text = "Task1\nContent1\n---\n## Contents:: \nContent2"
    tasks = process_input(input_text)
    assert tasks[0] == ('Summarize 1', 'Content1'), "First task should be ('Task1', 'Content1')"
    assert tasks[1] == ('Contents::', 'Content2'), "Second task should be ('Task2', 'Content2')"

    # Test with markdown headings as task types
    input_text = "# Task1\nContent1\n---\n## Task2\nContent2"
    tasks = process_input(input_text)
    assert tasks[0] == ('Task1', 'Content1'), "First task should be ('Task1', 'Content1')"
    assert tasks[1] == ('Task2', 'Content2'), "Second task should be ('Task2', 'Content2')"

    # Test with mixed markdown headings and default task types
    input_text = "Content without heading\n---\n#### 2\nContent 2!!"
    tasks = process_input(input_text)
    assert tasks[0] == ('Summarize 1', 'Content without heading'), "First task should be ('Task 1', 'Content without heading')"
    assert tasks[1] == ('2', 'Content 2!!'), "Second task should be ('Task2', 'Content2')"

    # Test with only default task types
    input_text = "Content without heading\n---\nMore content without heading"
    tasks = process_input(input_text)
    assert tasks[0] == ('Summarize 1', 'Content without heading'), "First task should be ('Task 1', 'Content without heading')"
    assert tasks[1] == ('Summarize 2', 'More content without heading'), "Second task should be ('Task 2', 'More content without heading')"


    # Test with 4 tasks: header only, content only, header and content, 2nd header and content
    input_text = "# Header Only\n---\nOnly content without header\n---\n# Header and Content\nContent for header and content\n---\n## Second Header\nSecond header content"
    tasks = process_input(input_text)
    assert isinstance(tasks, list), "process_input should return a list"
    assert len(tasks) == 4, "process_input should return a list of four tasks"
    assert tasks[0] == ('Header Only', ''), "First task should be ('Header Only', '')"
    assert tasks[1] == ('Summarize 1', 'Only content without header'), "Second task should be ('Summarize 1', 'Only content without header')"
    assert tasks[2] == ('Header and Content', 'Content for header and content'), "Third task should be ('Header and Content', 'Content for header and content')"
    assert tasks[3] == ('Second Header', 'Second header content'), "Fourth task should be ('Second Header', 'Second header content')"

    # Test with empty string
    input_text = ""
    tasks = process_input(input_text)
    assert isinstance(tasks, list), "process_input should return a list"
    assert len(tasks) == 0, "process_input should return an empty list for empty input"


if __name__ == "__main__":
    pytest.main()