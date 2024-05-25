import os
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

# Set up API keys for various providers
api_keys = {
    'openai': os.environ.get('OPENAI_API_KEY'),
    'groq': os.environ.get('GROQ_API_KEY'),
    # Add more providers as needed
    # 'provider_name': os.environ.get('PROVIDER_API_KEY'),
}

# Define a dictionary of prompts for different task types
PROMPTS = {
    "Summarize": """Summarize the content and give the output in an instructive way like you are teaching me."""
}

# Define a dictionary to map engines to their default models
default_models = {
'groq': 'llama3-70b-8192',
'openai': 'gpt-3.5-turbo-1106'
}

# Define a dictionary to map engines to their corresponding classes
engine_classes = {
'groq': ChatGroq,
'openai': ChatOpenAI
}

'''
• RPM: Requests Per Minute. The number of requests you can make to the model per minute.
• TPM: Tokens Per Minute. The number of tokens you can process per minute.
• BQL: Batch Query Limit. The maximum number of queries you can process in a batch, which is a group of requests sent together to the model.

| Model                     | Input Cost (/1M tokens) | Output Cost (/1M tokens) | Total Cost (/1M tokens) | Rate Limits                             |
|---------------------------|-------------------------|--------------------------|--------------------------|--------------------------------------- |
| open-mistral-7b           | $0.25                   | $0.25                    | $0.50                    | 5 requests/sec, 2M TPM, 10,000M/month  |
| open-mixtral-8x7b         | $0.70                   | $0.70                    | $1.40                    | 5 requests/sec, 2M TPM, 10,000M/month  |
| gpt-4-turbo               | $0.50                   | $1.50                    | $2.00                    | 5,000 RPM, 600,000 TPM, 40,000,000 BQL |
| gpt-3.5-turbo             | $0.50                   | $1.50                    | $2.00                    | 3,500 RPM, 160,000 TPM, 10,000,000 BQL |
| mistral-small             | $1.00                   | $3.00                    | $4.00                    | 5 requests/sec, 2M TPM, 10,000M/month  |
| open-mixtral-8x22b        | $2.00                   | $6.00                    | $8.00                    | 5 requests/sec, 2M TPM, 10,000M/month  |
| mistral-medium            | $2.70                   | $8.10                    | $10.80                   | 5 requests/sec, 2M TPM, 10,000M/month  |
| mistral-large             | $4.00                   | $12.00                   | $16.00                   | 5 requests/sec, 2M TPM, 10,000M/month  |
| gpt-4                     | $3.00                   | $15.00                   | $18.00                   | 5,000 RPM, 80,000 TPM, 5,000,000 BQL   |
| llama3-70b-8192 (Groq)    | Free                    | Free                     | Free                     | 30 RPM, 14,400 Requests/day, 6,000 TPM |
| llama3-8b-8192 (Groq)     | Free                    | Free                     | Free                     | 30 RPM, 14,400 Requests/day, 30,000 TPM|
| gemma-7b-it (Groq)        | Free                    | Free                     | Free                     | 30 RPM, 14,400 Requests/day, 15,000 TPM|
| mixtral-8x7b-32768 (Groq) | Free                    | Free                     | Free                     | 30 RPM, 14,400 Requests/day, 5,000 TPM |
'''