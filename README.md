# LangChain Workflows

LangChain Workflows is a Python-based project that leverages advanced language models to generate concise workflow prompts from input text. It provides a streamlined process from reading and processing input to generating and saving workflow prompts, making it a powerful tool for text analysis and information extraction.

## Project Structure

The project is structured as follows:

- `langchain_env/`: Main project directory
  - `configs.py`: Contains the API key setup and the dictionary of prompts.
  - `models.py`: Contains the ResponseModel Pydantic model.
  - `input_processing.py`: Contains functions for reading input and processing tasks.
  - `output_generation.py`: Contains the function for generating output using language models.
  - `file_operations.py`: Contains functions for saving results to a Markdown file.
  - `main.py`: The main script to orchestrate the process.
- `tests/`: Contains test files for the project.
- `Input-Output/`: Contains input and output files.

## Usage

To use this project, follow these steps:

1. Make sure you have `conda` installed on your system.
2. Clone the repository and navigate to the project directory.
3. Set up the environment using the `environment.yml` file:

   ```
   conda env create -f environment.yml
   ```
4. Activate the newly created environment:

   ```
   conda activate langchain-env
   ```
5. Set up API keys for various providers by setting environment variables:

   - For macOS/Linux (add to .bashrc, .zshrc, or equivalent):
     ```
     export OPENAI_API_KEY='your_openai_api_key'
     export GROQ_API_KEY='your_groq_api_key'
     export COHERE_API_KEY='your_cohere_api_key'
     export MISTRAL_API_KEY='your_mistral_api_key'
     # Add more providers as needed
     ```
   - For Windows (set environment variables in the command prompt or PowerShell):
     ```cmd
     setx OPENAI_API_KEY "your_openai_api_key"
     setx GROQ_API_KEY "your_groq_api_key"
     setx COHERE_API_KEY "your_cohere_api_key"
     setx MISTRAL_API_KEY "your_mistral_api_key"
     REM Add more providers as needed
     ```
6. Install all the dependencies using `poetry`. All dependencies are listed in the `pyproject.toml` file:

   ```
   poetry install
   ```
7. Prepare your input text file and place it in the `Input-Output/` directory.
8. Run the `main.py` script. This will read the input file, process the tasks, generate the output, and save it to an output file in the `Input-Output/` directory.

## Contributing

Contributions are welcome. Please submit a pull request or open an issue to discuss your changes.

## License

This project is licensed under the terms of the MIT license.
