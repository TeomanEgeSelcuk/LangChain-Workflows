from langchain_core.pydantic_v1 import BaseModel, Field

# Define the default Pydantic model
class SummarizeModel(BaseModel):
    title: str = Field(description="Title of the summary generated, have it be very short")
    text: str = Field(description="Text of the summary generated in an instructive way like you are teaching me")

