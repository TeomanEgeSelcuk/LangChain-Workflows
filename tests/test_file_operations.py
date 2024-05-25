import os
import pytest
from langchain_env.file_operations import save_as_markdown
from typing import List, Tuple

# Test cases for save_as_markdown function
def test_save_as_markdown_basic():
    results = [
        ("Summarize", "This is task 1 content", {"title": "Task 1 Title", "text": "Task 1 Summary"}),
        ("Summarize", "This is task 2 content", {"title": "Task 2 Title", "text": "Task 2 Summary"})
    ]
    filename = "test_output_basic.md"
    save_as_markdown(results, filename)
    
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, 'Input-Output', filename)

    with open(file_path, 'r') as file:
        content = file.read()
    
    expected_content = (
        "### Task 1 Title\n"
        "<details>\n"
        "<summary>Task 1 Summary</summary>\n\n"
        "</details>\n\n"
        "### Task 2 Title\n"
        "<details>\n"
        "<summary>Task 2 Summary</summary>\n\n"
        "</details>\n\n"
    )
    
    assert content == expected_content
    os.remove(file_path)

def test_save_as_markdown_empty():
    results = []
    filename = "test_output_empty.md"
    save_as_markdown(results, filename)
    
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, 'Input-Output', filename)

    with open(file_path, 'r') as file:
        content = file.read()
    
    assert content == ""
    os.remove(file_path)

def test_save_as_markdown_special_characters():
    results = [
        ("Summarize", "Content with special char & < > \" '", {"title": "Task with special char & < > \" '", "text": "Summary with special char & < > \" '"}),
    ]
    filename = "test_output_special_characters.md"
    save_as_markdown(results, filename)
    
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, 'Input-Output', filename)

    with open(file_path, 'r') as file:
        content = file.read()
    
    expected_content = (
        "### Task with special char & < > \" '\n"
        "<details>\n"
        "<summary>Summary with special char & < > \" '</summary>\n\n"
        "</details>\n\n"
    )
    
    assert content == expected_content
    os.remove(file_path)

def test_save_as_markdown_large_input():
    results = [
        ("Summarize", "Large content" * 1000, {"title": "Task Large", "text": "Summary Large" * 1000}),
    ]
    filename = "test_output_large.md"
    save_as_markdown(results, filename)
    
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, 'Input-Output', filename)

    with open(file_path, 'r') as file:
        content = file.read()
    
    expected_content = (
        "### Task Large\n"
        "<details>\n"
        "<summary>" + "Summary Large" * 1000 + "</summary>\n\n"
        "</details>\n\n"
    )
    
    assert content == expected_content
    os.remove(file_path)

if __name__ == "__main__":
    pytest.main()
