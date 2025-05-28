"""Execute LLM prompt in Mistral"""

import os
from typing import List

from mistralai import Mistral

MISTRAL_API_KEY = os.getenv("LLM_API_KEY")
MODEL = "mistral-large-latest"
client = Mistral(api_key=MISTRAL_API_KEY)


def execute_prompts(prompts: List[str]) -> List[str]:
    """Execute prompt in Mistral LLM

    Args:
        prompts (List[str]): List of prompts to execute

    Returns:
        List[str]: List of answer from Mistral LLM
    """
    answers: List[str] = []
    for prompt in prompts:
        chat_response = client.chat.complete(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        answer = (
            chat_response.choices[0]
            .message.content.replace("```json", "")
            .replace("```", "")
        )
        answers.append(answer)
    return answers
