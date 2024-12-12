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
# llm = os.getenv('LLM_MODEL', 'gpt-4o')
llm = 'qwen2.5-coder:0.5b'

client = AsyncOpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama'
)

model = OpenAIModel(llm) if llm.lower().startswith("gpt") else OpenAIModel(llm, openai_client=client)

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
# logfire.configure(send_to_logfire='if-token-present')


@dataclass
class Deps:
    client: AsyncClient
    brave_api_key: str | None
    
    
class RiskyFeature(BaseModel):
    # feature: str = Field(..., description="The name of the feature")
    is_risky: bool = Field(..., description="Whether the feature can cause an ethical risk")
    risk_level: Annotated[int, Field(ge=0, le=10,description="The risk level of the feature, from 0 to 10")]
    justification: str = Field(..., description="Justification for the risk level")
    # recommendation: str = Field(..., description="Recommendation for handling the risk")
    
class Test(BaseModel):
    # response: str
    joke: str
    answer: str
    
class RiskyFeatures(BaseModel):
    features: list[RiskyFeature]



with open('./ai_agent/system_prompt.txt', 'r') as f:
    system_prompt = f.read()

risky_feature_detector = Agent(
    'ollama:llama3.2',
    system_prompt=system_prompt,
    retries=10,
    result_type=RiskyFeature
)

