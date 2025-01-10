from __future__ import annotations as _annotations

import asyncio
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Annotated

from devtools import debug
from httpx import AsyncClient
from dotenv import load_dotenv

from openai import AsyncOpenAI
from pydantic import BaseModel, Field
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai import Agent, ModelRetry, RunContext

from pandas import DataFrame

load_dotenv()
llm = os.getenv('LLM_MODEL', 'mistral:latest')
# llm = "qwen2.5-coder:0.5b"

client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# model = OpenAIModel(llm, openai_client=client)
model = (
    OpenAIModel(llm)
    if llm.lower().startswith("gpt")
    else OpenAIModel(llm, openai_client=client)
)

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
# logfire.configure(send_to_logfire='if-token-present')


@dataclass
class Deps:
    client: AsyncClient
    brave_api_key: str | None


class Feature(BaseModel):
    """
    A feature is a variable in the dataset that is potentially risky.
    """

    # feature: str = Field(..., description="The name of the feature")
    is_sensitive: bool = Field(..., description="Whether the feature is sensitive")
    sensibility_level: Annotated[
        int, Field(ge=0, le=10, description="The sensibility level of the feature")
    ]
    justification: str = Field(..., description="Justification for the risk level")
    recommendation: str = Field(..., description="Recommendation for handling the risk")


class Test(BaseModel):
    # response: str
    joke: str
    answer: str


class Features(BaseModel):
    features: list[Feature]


with open("./ai_agent/system_prompt.txt", "r") as f:
    system_prompt = f.read()

risky_feature_detector = Agent(
    model=model,
    # system_prompt=system_prompt,
    system_prompt="""You are an experimented data scientist. You are given a feature of a dataset and some contextual information about the dataset. 
    Identifies if the feature is potentially sensitive. Indicates whether a column contains information that is personal, confidential, 
    or likely to reveal details of a person's ethnic origin, political opinions, health, financial data, or any other sensitive characteristic that could be used to discriminate against certain groups.
    Take into account the description of the dataset and the context of the feature.
    You need to provide a score between 0 and 10 for the feature, a justification for the score, and a recommendation for how to handle the risk. 
    The score is the sensibility level of the feature. A higher score indicates a higher risk of bias. 
    The justification should be a short explanation of the reasoning behind the score. 
    Your response should be in JSON format. Provide the response in the following format: {"sensibility_level": <score>, "justification": "<justification>", "recommendation": "<recommendation>"}""",
    retries=10,
    result_type=Feature,
)
