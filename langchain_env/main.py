from input_processing import read_input, process_input
from output_generation import generate_output
from file_operations import save_as_markdown

'''
This code defines the main function that orchestrates the overall process.
It reads input from a file, processes the input, prompts the user to choose an engine,
generates output using the chosen engine, and saves the results to an output file.
----------------
1. config.py: Contains the API key setup and the dictionary of prompts.
2. models.py: Contains the ResponseModel Pydantic model.
3. input_processing.py: Contains functions for reading input and processing tasks.
4. output_generation.py: Contains the function for generating output using language models.
5. file_operations.py: Contains functions for saving results to a Markdown file.
6. main.py: The main script to orchestrate the process.
'''

def main():
    """
    Main function that orchestrates the overall process.
    """
    input_filename = 'input.md'  # Name of the input file
    output_filename = 'output.md'  # Name of the output file

    input_text = read_input(input_filename)  # Read input from the input file
    tasks = process_input(input_text)  # Process the input text to extract tasks
    # Generate output using the chosen engine. Engine is not mandatory to be passed as an argument, defaults to groq.
    # Options for engine: 'openrouter' or 'groq'. Set it like this: engine='groq' or engine='openrouter'. 
    results = generate_output(tasks) 
    save_as_markdown(results, output_filename)  # Save the results to the output file

if __name__ == "__main__":
    main()
