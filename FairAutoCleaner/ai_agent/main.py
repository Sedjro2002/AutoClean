from __future__ import annotations as _annotations

import asyncio
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Annotated

from httpx import AsyncClient
from dotenv import load_dotenv
from pathlib import Path

from openai import AsyncOpenAI
from pydantic import BaseModel, Field
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai import Agent

load_dotenv()
# llm = os.getenv('LLM_MODEL', 'llama3.2:3b')
llm = os.getenv('LLM_MODEL', 'deepseek-chat')
# llm = "qwen2.5-coder:0.5b"
base_url = os.getenv('BASE_URL', 'https://api.deepseek.com/v1')
api_key = os.getenv('API_KEY', 'sk-feab401304ce4af48849c9e630511d48') #TODO to change
# client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
client = AsyncOpenAI(base_url=base_url, api_key=api_key)

# model = OpenAIModel(llm, openai_client=client)
model = (
    OpenAIModel(llm)
    if llm.lower().startswith("gpt")
    else OpenAIModel(llm, openai_client=client)
)

system_prompt_path = Path(__file__).parent / "system_prompt.txt"

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
    justification: str | None = Field(None, description="Justification if the feature is sensitive")
    recommendation: str | None = Field(None, description="Recommendation for handling the risk if the feature is sensitive")


class Features(BaseModel):
    features: list[Feature]


with open(system_prompt_path, "r") as f:
    system_prompt = f.read()

risky_feature_detector = Agent(
    model=model,
    system_prompt=system_prompt,
    retries=10,
    result_type=Feature,
)
