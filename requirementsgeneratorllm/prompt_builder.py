"""Module creating the prompt command for LLM"""

from typing import List

from requirementsgeneratorllm.constants import REQUIREMENT_TYPES


def build_prompts(
    project_description: str,
    requirement_types: List[str],
    selected_countries: List[str],
    selected_language: str,
) -> List[str]:
    prompts: List[str] = []
    for requirement_type in requirement_types:
        requirement_type_data = REQUIREMENT_TYPES.get(requirement_type, None)
        if requirement_type_data is not None:
            prompt = f"""
                You're an expert of standards such as IREB, IIBA (International Institute of Business Analysis) best practices.
                Your skills in systems engineering, functional modeling, business analysis and regulatory documentation enable you to write specifications that are perfectly structured, standardized and directly usable by technical teams.
                Given the project description and user input below, generate clear, categorized software requirements:

                To do this, you will carry out the following actions:
                1. Look for examples of requirements, if publicly available, to get inspiration from their structure, vocabulary and formalism.
                2. Generate an exhaustive list of requirements in {selected_language}, covering all classic, limit and alternative use cases.
                3. Structure each requirement in one of the following formats:
                - The system shall SUBJECT
                - The system shall allow the user to SUBJECT
                - When the user CONDITION, the system shall SUBJECT
                4. Each requirement must be SMART:
                - A requirement specifies what the system must do
                - A requirement is measurable, so you can tell if the system does it
                - A requirement is achievable within the timeframe you've set yourself
                - A requirement is relevant to your business objectives
                - A requirement is time-bound so you can monitor progress
                5. Avoid usage of fancy words like "too", "much", "little", "more", "robust", "etc."
                6. If your requirements content includes a "and" or a "or", divide the requirement.
                - For example, "The system shall allow the user to add and remove an article description" should be divided to "The system shall allow the user to add an article description" and "The system shall allow the user to remove an article description"
                7. Gives specifications only for the specified 'Requirement Type'. Don't stray from the requirement!
                
                Project Description:
                {project_description}

                Selected Requirement Type:
                {requirement_type_data.llm_description}

                Please output the requirements grouped by category in plain text format.

                Important rule: carry out all the actions without interrupting yourself or asking for my opinion. Don't stop until you've completed the task in question, meeting the following criteria.
            """
            if selected_countries:
                joined_countries = ", ".join(selected_countries)
                prompt += f"""
                    Deployment Countries:
                    For countries of deployment, search the Internet for regulations that apply to the project.
                    {joined_countries}
                """
            prompts.append(prompt)
    return prompts
