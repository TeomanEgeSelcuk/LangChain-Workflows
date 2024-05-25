from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from typing import List, Dict, Tuple
import pprint

# Files 
from langchain_env.configs import PROMPTS, engine_classes, default_models
from langchain_env.models import *

def generate_output(engine: str = 'groq', model_name: str = None, pydantic_object: BaseModel = SummarizeModel, tasks: List[Dict[str, str]] = None) -> List[Tuple[str, str, Dict]]:
    """
    Calls a language model to extract information from a given phrase using a JSON output parser.

    Args:
        engine (str, optional): The engine to use. Defaults to 'groq'.
        model_name (str, optional): The model to use. Defaults to 'Llama3-70b-8192' for 'groq' and 'gpt-3.5-turbo-1106' for 'openai'.
        pydantic_object (BaseModel, optional): The Pydantic model to structure the extracted information. Defaults to SummarizeModel.
        tasks (List[Dict[str, str]], optional): A list of tasks where each task is a dictionary with 'task_type' and 'content' keys. Defaults to None.

    Returns:
        List[Tuple[str, str, Dict]]: A list of tuples where each tuple contains the task type, content, and the generated dictionary.
    """

    # Initialize the JSON output parser with the Pydantic model
    parser = JsonOutputParser(pydantic_object=pydantic_object)

    if tasks is None:
        tasks = [("Summarize", "The ingredients for a Margherita pizza are tomatoes, onions, cheese, basil")]

    # If model_name is not provided, set it based on the engine
    model_name = model_name or default_models.get(engine)

    # Initialize the model based on the engine, using the specified or default model_name
    model_class = engine_classes.get(engine)
    if model_class:
        model = model_class(model=model_name, temperature=0.7)

    # Initialize the OutputFixingParser with the JSON output parser
    parser = OutputFixingParser.from_llm(parser=parser, llm=model, max_retries=2)

    results = []

    for task_type, content in tasks:
        # Get the corresponding prompt for the task type
        if task_type.lower() in (prompt.lower() for prompt in PROMPTS):
            prompt_text = PROMPTS[task_type]
        else:
            raise ValueError(f"Task type '{task_type}' not found in PROMPTS dictionary.")
        
        # Create a ChatPromptTemplate instance from a list of messages
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"{prompt_text}\nFormatting Instructions: {{format_instructions}}"),
            ("human", "{phrase}")
        ])

        # Create the processing chain: prompt -> model -> parser
        chain = prompt | model | parser

        # Invoke the chain with the given input and format instructions
        result = chain.invoke({
            "phrase": content,
            "format_instructions": parser.get_format_instructions()
        })

        results.append((task_type, content, result))

    return results

def main():
    """
    Main function to evaluate test cases for both OpenAI and Groq models.
    
    This function defines a set of test cases and uses the `generate_output` function to 
    generate summaries for these cases using both OpenAI and Groq models. The results are 
    then printed.
    """
    # Define test cases
    test_cases = [
        ("Summarize", """
        The 'coverage score' is calculated as the percentage of assessment questions
        for which both the summary and the original document provide a 'yes' answer.
        This method ensures that the summary not only includes key information from the original
        text but also accurately represents it. A higher coverage score indicates a
        more comprehensive and faithful summary, signifying that the summary effectively
        encapsulates the crucial points and details from the original content.
        """),
        ("Summarize", """
        The 'alignment score' determines whether the summary contains hallucinated or
        contradictory information to the original text. This method ensures that the
        summary is consistent with the original document and does not introduce new
        information that is not present in the original text.
        """)
    ]

    # Evaluate test cases for Groq  llama3-70b-8192
    print("Evaluating Groq llama3-70b-8192 model:")
    results_groq = generate_output(engine="groq", model_name='llama3-8b-8192', tasks=test_cases)
    # results_groq = generate_output(engine="openai", tasks=test_cases)
    for result in results_groq:
        pprint.pprint(result)


# Run the main function
if __name__ == "__main__":
    main()

# result output 
'''
{'properties': {'text': {'description': 'Text of the summary generated in an '
                                        'instructive way like you are teaching '
                                        'me',
                         'title': 'Text',
                         'type': 'string'},
                'title': {'description': 'Title of the summary generated, have '
                                         'it be very short',
                          'title': 'Title',
                          'type': 'string'}},
 'required': ['title', 'text']}
{'text': 'The alignment score determines whether the summary contains '
         'hallucinated or contradictory information to the original text. This '
         'method ensures that the summary is consistent with the original '
         'document and does not introduce new information that is not present '
         'in the original text.',
 'title': 'Summary of Alignment Score'}
'''